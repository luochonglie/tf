#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/08 16:33
# @Author  : c0l0121
# @File    : seed_classifier.py
# @Desc    :


import numpy as np
import json


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


def load_data():
    data = np.genfromtxt("../../dataset/mlsd/ch02/seeds_dataset.txt", delimiter=",", comments='#')
    features = data[:, :7].copy()
    labels = data[:, 7:].copy()

    # Reading data back
    with open("../../dataset/mlsd/ch02/seeds_desc.txt", 'r') as f:
        data1 = json.load(f, object_hook=JSONObject)
        feature_names = data1.feature_names
        label_names = data1.label_names

    return features, labels, feature_names, label_names


def classify(features, labels, feature_names, label_names):
    print(1)


def main():
    features, labels, feature_names, label_names = load_data()
    print(features)


if __name__ == "__main__":
    main()
