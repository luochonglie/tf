# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:09:58 2016
Test MNIST dataset
@author: liudiwei
"""

from sklearn import neighbors
from utils.mnist_utils import DataUtils
import datetime
import matplotlib.pyplot as plt
import numpy as np
import math


def main():
    start_time = datetime.datetime.now()

    training_image = '../../dataset/MNIST/train-images.idx3-ubyte'
    training_label = '../../dataset/MNIST/train-labels.idx1-ubyte'
    testfile_image = '../../dataset/MNIST/t10k-images.idx3-ubyte'
    testfile_label = '../../dataset/MNIST/t10k-labels.idx1-ubyte'
    train_image = DataUtils(filename=training_image).get_images()
    train_label = DataUtils(filename=training_label).get_labels()
    test_image = DataUtils(testfile_image).get_images()
    test_label = DataUtils(testfile_label).get_labels()

    end_time = datetime.datetime.now()
    print('Load data use time: ' + str(end_time - start_time))

    return train_image, train_label, test_image, test_label


def classify_and_show():
    train_images, train_labels, test_images, test_labels = main()

    k = 3
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_images, train_labels)

    length = 5
    start_idx = np.random.randint(0, 10000 - length)
    end_idx = start_idx + length

    predict_label = knn.predict(test_images[start_idx:end_idx])
    k_neighbors = knn.kneighbors(test_images[start_idx:end_idx], k, False)
    print(k_neighbors)
    k_neighbor_images = []
    k_neighbor_labels = []

    for i in np.nditer(np.array(k_neighbors)):
        k_neighbor_images.append(train_images[i])
        k_neighbor_labels.append(train_labels[i])

    show_images(test_images[start_idx:end_idx], predict_label, k_neighbor_images, k_neighbor_labels, k)


def show_images(test_images, test_labels, train_images, train_labels, k):
    for i in range(len(test_images)):
        plt.figure(num='Test Image:' + str(i), figsize=(6, 6))  # 创建一个名为astronaut的窗口,并设置大小
        row = 2
        col = math.ceil((k + 1) / 2.0)

        img = np.array(test_images[i])
        img = img.reshape(28, 28)
        plt.subplot(row, col, 1)  # 将窗口分为两行两列四个子图，则可显示四幅图片
        plt.title('Test  img: ' + str(test_labels[i]))  # 第一幅图片标题
        plt.imshow(img, cmap='binary')  # 将图像黑白显示  # 绘制第一幅图片

        for j in range(k):
            img = np.array(train_images[(i * k) + j])
            img = img.reshape(28, 28)
            plt.subplot(row, col, j + 2)  # 第二个子图
            plt.title('Train img: ' + str(train_labels[(i * k) + j]))  # 第二幅图片标题
            plt.imshow(img, cmap='binary')  # 绘制第二幅图片,且为灰度图
            # plt.axis('off')  # 不显示坐标尺寸

    plt.show()  # 显示窗口


if __name__ == "__main__":
    classify_and_show()