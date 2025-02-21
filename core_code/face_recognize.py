import os
import sys

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import pickle
from net import *
from face_alignment import mtcnn
from face_alignment import align
import numpy as np
from PIL import Image
import torch
import cv2


class face_detector:

    def __init__(
        self,
        architecture="ir_101",
        face_features_path=r"H:\600-副业\千墨科技\01.人脸识别\AdaFace\core_code\face_feature_lib\star_face_features.pkl",
        device="cuda:0",
        threshold=0.26,
    ):
        self.adaface_models = {
            "ir_101": r"H:\600-副业\千墨科技\01.人脸识别\AdaFace\core_code\pretrained_model\adaface_ir101_ms1mv2.ckpt",
        }
        self.architecture = architecture
        self.face_features_path = face_features_path
        self.device = device
        self.threshold = threshold
        self._init_process()

    def _init_process(self):
        with open(self.face_features_path, "rb") as f:
            self.face_features = pickle.load(f)

        self.adaface_model = self._load_pretrained_model()
        self.mtcnn_model = mtcnn.MTCNN(device=self.device, crop_size=(112, 112))

        self.face_features_tensor, self.mask, self.name_list = self._arange_to_tensor()

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

    # ----------下面是自己写的函数------------------
    def get_multiple_aligned_faces(self, image_path, rgb_pil_image=None):
        if rgb_pil_image is None:
            img = Image.fromarray(frame_rgb)
            img = img.convert("RGB")
            # img = Image.open(image_path).convert("RGB")
        else:
            assert isinstance(
                rgb_pil_image, Image.Image
            ), "Face alignment module requires PIL image or path to the image"
            img = rgb_pil_image
        # find face
        try:
            bboxes, faces = self.mtcnn_model.align_multi(img, limit=None)
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

    @torch.no_grad()
    def get_detect_results(self, frame_rgb):
        # 这是主函数
        bboxes, aligned_rgb_imgs = align.get_multiple_aligned_faces(frame_rgb)
        print("得到人脸的数量", len(bboxes))
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


if __name__ == "__main__":
    image_path = "./datasets/test/胡歌1.jpg"
    frame = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    # frame = cv2.imread(image_path)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detector = face_detector()
    print("检测器检测结果", detector.get_detect_results(frame_rgb))
