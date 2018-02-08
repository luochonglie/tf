#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/01/24 11:08
# @Author  : c0l0121
# @File    : iris_classifier.py
# @Desc    : Classify Iris

import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

IS_DEBUG = False
IDX_SEPAL_LENGTH = 0
IDX_SEPAL_WIDTH = 1
IDX_PETAL_LENGTH = 2
IDX_PETAL_WIDTH = 3

LABEL_SETOSA = 0
LABEL_VERSICOLOR = 1
LABEL_VIRGINICA = 2


def load_data():
    data = load_iris()
    if IS_DEBUG:
        print_iris_data(data)
    return data['data'], data['feature_names'], data['target'], data['target_names']


def print_iris_data(data):
    for i in data:
        print(i, "=", data[i])


def draw_features(features, feature_names, labels, label_names):
    for i in range(len(feature_names)):
        for j in range(i + 1, len(feature_names)):
            for t, marker, c in zip(range(3), '>ox', 'rgb'):
                # 我们画出每个类别，它们各自采用不同的颜色标识
                plt.scatter(features[labels == t, i], features[labels == t, j], marker=marker,
                            c=c)
                plt.xlabel(feature_names[i])
                plt.ylabel(feature_names[j])
            plt.show()


def analysis(features, feature_names, labels, label_names):
    # draw_features(features, feature_names, labels, label_names)

    # 花瓣长度
    petal_length = features[:, 2]
    is_setosa = (labels == LABEL_SETOSA)

    print("Maximum petal length of setosa = {0}.".format(np.max(petal_length[is_setosa])))
    print("Minimum petal length of others = {0}.".format(np.min(petal_length[~is_setosa])))

    # Virginica & Versicolor features
    vv_features = features[~is_setosa]
    vv_labels = labels[~is_setosa]
    print("len(vv_features) = ", len(vv_features))
    print("len(vv_labels) = ", len(vv_labels))
    # 构造标识virginica对象序号的数组
    is_virginica = (vv_labels == LABEL_VIRGINICA)
    print("is_virginica = ", is_virginica)
    print("vv_features.shape = ", np.shape(vv_features))

    best_acc = -1.0
    best_fi = -1
    best_t = -1

    for fi in range(np.shape(vv_features)[1]):
        thresh = np.array(features)[:, fi].copy()
        thresh.sort()
        for t in thresh:
            predict = (vv_features[:, fi] > t)
            acc = (predict == is_virginica).mean()
            if acc > best_acc:
                best_acc = acc
                best_fi = fi
                best_t = t

    print("best_f = %d" % best_fi)
    print("best_t = %f" % best_t)
    print("best_acc = %f" % best_acc)
    print(feature_names[best_fi])


def classify(features, label_names):
    pre_labels = []
    pre_label_names = []

    petal_length_threshold_for_setosa = 2.0
    petal_with_threshold_for_virginica = 1.6

    for idx in range(np.shape(features)[0]):
        if features[idx][IDX_PETAL_LENGTH] < petal_length_threshold_for_setosa:
            pre_labels.append(LABEL_SETOSA)
        else:
            if features[idx][IDX_PETAL_WIDTH] > petal_with_threshold_for_virginica:
                pre_labels.append(LABEL_VIRGINICA)
            else:
                pre_labels.append(LABEL_VERSICOLOR)

        pre_label_names.append(label_names[pre_labels[-1]])

    return pre_labels, pre_label_names


def main():
    features, feature_names, labels, label_names = load_data()

    analysis(features, feature_names, labels, label_names)

    pre_labels, pre_label_names = classify(features, label_names)
    print("error rate = %f" % (1 - (pre_labels == labels).mean()))


if __name__ == "__main__":
    IS_DEBUG = True
    main()
