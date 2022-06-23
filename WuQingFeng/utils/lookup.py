import h5py
import numpy as np
from numpy import linalg as LA
from pathlib import Path
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import os
from PIL import Image


class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.weight = 'imagenet'
        self.pooling = 'max'
        self.model = VGG16(weights=self.weight,
                           input_shape=(self.input_shape[0], self.input_shape[1], self.input_shape[2]),
                           pooling=self.pooling, include_top=False)
        self.model.predict(np.zeros((1, 224, 224, 3)))

    def extract_feat(self, image_content):
        img = np.expand_dims(image_content, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        norm_feat = feat[0] / LA.norm(feat[0])
        return norm_feat


def lookup(query):
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_name = str(BASE_DIR) + '/utils/lol.h5'
    print(file_name)
    h5f = h5py.File(file_name, 'r')
    feats = h5f['dataset_1'][:]  # 从文件中拿出所有的特征
    imgNames = h5f['dataset_2'][:]  # 从文件中拿出所有特征对应的图片名字
    h5f.close()
    model = VGGNet()
    queryVec = model.extract_feat(query)
    scores = np.dot(queryVec, feats.T)  # 所有图片与测试图片匹配出来的概率
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]  # 对概率做排序
    maxres = 28
    imlist = [imgNames[index] for i, index in enumerate(rank_ID[0:maxres])]  # 对应的图片名字
    return {'image_name': imlist, 'probability': rank_score}
