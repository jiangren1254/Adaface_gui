"""
    获取人脸特征
    获得一个人脸特征库
"""

import torch
import os
import sys
import sqlite3
from PIL import Image
import io

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
import net
from face_alignment import align
import numpy as np
import pickle

# TODO: add model
adaface_models = {
    "ir_101": "./pretrained_model/adaface_ir101_ms1mv2.ckpt",
}


def load_pretrained_model(architecture="ir_101"):
    # load model and pretrained statedict
    assert architecture in adaface_models.keys()
    model = net.build_model(architecture)
    statedict = torch.load(adaface_models[architecture])["state_dict"]
    model_statedict = {
        key[6:]: val for key, val in statedict.items() if key.startswith("model.")
    }
    model.load_state_dict(model_statedict)
    model.eval()
    return model


def to_input(pil_rgb_image):
    np_img = np.array(pil_rgb_image)
    brg_img = ((np_img[:, :, ::-1] / 255.0) - 0.5) / 0.5
    tensor = torch.tensor(brg_img.transpose(2, 0, 1)).float()
    return tensor.unsqueeze(0)


if __name__ == "__main__":

    model = load_pretrained_model("ir_101").to(0)
    individual_root = "datasets/train"
    features_dic = {}
    features_file = "face_feature_lib/star_face_features.pkl"

    # with torch.no_grad():
    #     for name in os.listdir(individual_root):
    #         print(name)
    #         features_dic[name] = []
    #         for fname in sorted(os.listdir(os.path.join(individual_root, name))):
    #             path = os.path.join(individual_root, name, fname)
    #             aligned_rgb_img = align.get_aligned_face(path)
    #             if aligned_rgb_img == None:
    #                 continue
    #             try:
    #                 bgr_tensor_input = to_input(aligned_rgb_img)
    #                 feature, _ = model(bgr_tensor_input.to(0))
    #                 print("feature shape:", feature.shape)
    #                 features_dic[name].append(feature.cpu())
    #             except:
    #                 raise RuntimeError("Extract feature failed!")

    #         features_dic[name] = torch.cat(features_dic[name], dim=0)
    with torch.no_grad():
        conn = sqlite3.connect("./gui/face_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, id_card,image FROM face_data")
        data_list = cursor.fetchall()
        for name,id_card, img_blob in data_list:
            print(name,id_card)
            features_dic[name] = [] #(起名字时不能重复，如果同名，名字后面加入1,2,3)
            if img_blob is not None:
                rgb_pil_image = Image.open(io.BytesIO(img_blob)).convert("RGB")
                aligned_rgb_img = align.get_aligned_face(image_path=None, rgb_pil_image=rgb_pil_image)
                if aligned_rgb_img is None:
                    raise RuntimeError("检测人脸图像中是否有遮挡!")
                try:
                    bgr_tensor_input = to_input(aligned_rgb_img)
                    feature, _ = model(bgr_tensor_input.to(0))
                    # print("feature shape:", feature.shape)
                    features_dic[name].append(feature.cpu())
                except:
                    raise RuntimeError("Extract feature failed!")
            features_dic[name] = torch.cat(features_dic[name], dim=0)
        conn.close()   
    pickle.dump(features_dic, open(features_file, "wb"))
    print(f"{features_file} saved")
