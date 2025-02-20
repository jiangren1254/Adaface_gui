import yaml
from dotmap import DotMap


import os
import sys

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # 治表不治里解决方案
# 获取 core_code 的上级目录路径，并添加到 sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import pickle
from net import *
from face_alignment import mtcnn
from face_alignment import align

import numpy as np
import time
import shutil
from PIL import Image
import torch
import cv2


class face_detector:

    def __init__(
        self,
        config,
        architecture="ir_101",
        face_features_path="./face_feature_lib/star_face_features.pkl",
        device="cuda:0",
        threshold=0.26,
        # visualize_path="./illegalInfo/illegalImage/policy_person",
        # name2class_path="./name2class.txt",
        # laws_dir="./laws",
    ):
        self.adaface_models = {
            "ir_101": "./pretrained_model/adaface_ir101_ms1mv2.ckpt",
        }
        self.architecture = architecture
        self.face_features_path = face_features_path
        self.device = device
        self.threshold = threshold
        # self.visualize_path = visualize_path
        # self.name2class_path = name2class_path
        # self.laws_dir = laws_dir
        self.config = config

        self._init_process()

    def _load_pretrained_model(self):
        # load model and pretrained statedict
        assert (
            self.architecture in self.adaface_models.keys()
        ), f"Architecture should be {list(self.adaface_models.keys())}"

        model = build_model(self.architecture)
        statedict = torch.load(
            self.adaface_models[self.architecture], map_location=self.device
        )["state_dict"]
        model_statedict = {
            key[6:]: val for key, val in statedict.items() if key.startswith("model.")
        }
        model.load_state_dict(model_statedict)
        model.eval()

        return model.to(self.device)

    def _init_process(self):

        # self.general_classifier = general_cls(self.config.classifier.cam_output_root, self.config.classifier.device)

        with open(self.face_features_path, "rb") as f:
            self.face_features = pickle.load(f)

        self.adaface_model = self._load_pretrained_model()
        self.mtcnn_model = mtcnn.MTCNN(device=self.device, crop_size=(112, 112))

        self.face_features_tensor, self.mask, self.name_list = self._arange_to_tensor()

        self.name2class = {}  # 读文件 name2class.txt
        with open(self.name2class_path, "r", encoding="utf-8") as f:
            items = f.read().split("\n")
            for item in items:
                name, clas = item.split(" ")
                self.name2class[name] = clas

        self.class2law = {}  # 定义了一个空字典 读取文件夹 ./laws 下的文件
        for file in os.listdir(self.laws_dir):
            if file == "Domestic_negative_policy_figures.txt":
                with open(
                    os.path.join(self.laws_dir, file), "r", encoding="utf-8"
                ) as f:
                    contents = f.read()
                    self.class2law["负面人物-国内负面人物-国内负面政治人物"] = contents
                    self.class2law["负面人物-国内负面人物-国内负面名人"] = contents
            if file == "Reactionary_splitting.txt":
                with open(
                    os.path.join(self.laws_dir, file), "r", encoding="utf-8"
                ) as f:
                    contents = f.read()
                    self.class2law["负面人物-国内负面人物-反动分裂"] = contents
            if file == "Sensitive_political_event.txt":
                with open(
                    os.path.join(self.laws_dir, file), "r", encoding="utf-8"
                ) as f:
                    contents = f.read()
                    self.class2law["负面人物-国内负面人物-敏感政治事件"] = contents
                    self.class2law["负面人物-国际负面人物-受制裁的外国人"] = contents
            if file == "leader.txt":
                with open(
                    os.path.join(self.laws_dir, file), "r", encoding="utf-8"
                ) as f:
                    contents = f.read()
                    self.class2law["丑化正面人物-核心领导人"] = contents
                    self.class2law["丑化正面人物-主要领导人"] = contents
                    self.class2law["丑化正面人物-领导人家属"] = contents

    def _arange_to_tensor(self):
        # pad face_features and generate mask
        name_list = list(self.face_features.keys())

        length = torch.tensor(
            [feat.shape[0] for feat in self.face_features.values()], dtype=torch.int32
        )
        max_len = torch.max(length).data.item()
        f_dim = list(self.face_features.items())[0][1].shape[-1]
        # generate mask
        mask = length.unsqueeze(-1).repeat(1, max_len) > torch.arange(
            max_len
        ).unsqueeze(0).repeat(len(name_list), 1)
        mask = mask.float()

        pad_face_features = torch.zeros(len(name_list), max_len, f_dim).float()
        for pad_feat, face_feat in zip(pad_face_features, self.face_features.values()):
            pad_feat[: face_feat.shape[0], :].copy_(face_feat)

        return pad_face_features.to(self.device), mask.to(self.device), name_list

    def get_multiple_aligned_faces(self, image_path, rgb_pil_image=None):
        # 得到多个对其的人脸
        if rgb_pil_image is None:
            img = Image.open(image_path).convert("RGB")
        else:
            assert isinstance(
                rgb_pil_image, Image.Image
            ), "Face alignment module requires PIL image or path to the image"
            img = rgb_pil_image
        # find face
        try:
            bboxes, faces = self.mtcnn_model.align_multi(img)
            return bboxes, faces
        except Exception as e:
            print("Face detection Failed due to error.")
            print(e)

    def to_input(self, pil_rgb_images):
        tensor_list = []
        for pil_rgb_image in pil_rgb_images:
            np_img = np.array(pil_rgb_image)
            brg_img = ((np_img[:, :, ::-1] / 255.0) - 0.5) / 0.5
            tensor = torch.tensor(brg_img.transpose(2, 0, 1)).float().unsqueeze(0)
            tensor_list.append(tensor)
        return torch.cat(tensor_list, dim=0)

    def get_result_dict(self, img_face_features):

        sum_sim_tensor = torch.sum(
            torch.einsum("id, jnd->ijn", img_face_features, self.face_features_tensor),
            dim=-1,
        )
        multi_mask = 1.0 / torch.sum(self.mask, dim=-1)

        result_dict = {}
        max_val, max_indices = torch.max(
            torch.einsum("ij, j->ij", sum_sim_tensor, multi_mask), dim=1
        )
        for val, indice in zip(max_val.cpu(), max_indices.cpu()):
            result_dict[self.name_list[indice.data.item()]] = val.data.item()

        # 返回结果字典
        return result_dict

    def check_idx(self):
        return len(os.listdir(self.visualize_path))

    def draw_boxes_and_names(self, img_path, face_list):
        # 画框与写名字
        img = cv2.imread(img_path)
        for item in face_list:
            sx1 = int(item[2][0])
            sy1 = int(item[2][1])
            sx2 = int(item[2][2])
            sy2 = int(item[2][3])
            cv2.rectangle(img, (sx1, sy1), (sx2, sy2), (0, 255, 0), 1)
            if int(item[2][1]) > 10:
                cv2.putText(
                    img,
                    item[0] + str(item[1]),
                    (int(sx1), int(sy1 - 6)),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    0.5,
                    (0, 0, 255),
                )
            else:
                cv2.putText(
                    img,
                    item[0] + str(item[1]),
                    (int(sx1), int(sy1 + 15)),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    0.5,
                    (0, 0, 255),
                )

        # cv2.imwrite(detailed_img_path, img)
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return img

    @torch.no_grad()
    def get_detect_results(self, frame_rgb):
        bboxes, aligned_rgb_imgs = align.get_multiple_aligned_faces(frame_rgb)
        # print("得到人脸的数量",len(bboxes))
        if len(bboxes) == 0:
            # print(f"dected result: bboxes = 0")
            return []
        bgr_tensor_inputs = self.to_input(aligned_rgb_imgs)
        img_face_features, _ = self.adaface_model(bgr_tensor_inputs.to(self.device))

        result_dict = self.get_result_dict(img_face_features)
        # print(f'result_dict is {result_dict}')
        face_list = []
        for face_idx, (name, sim) in enumerate(result_dict.items()):
            if sim >= self.threshold:
                # sim是相似度
                face_list.append([name, sim, list(bboxes[face_idx])])

        if len(face_list) == 0:
            # print(f"dected result: in image is not face")
            return []
        return face_list


def get_config():
    with open("./config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return DotMap(config)


if __name__ == "__main__":
    image_path = "cam_output/our_data1/test/Sun_Kunkun/2.jpg"
    frame = cv2.imread(image_path)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detector = face_detector(get_config())
    print("检测器检测结果", detector.get_detect_results(frame_rgb))
