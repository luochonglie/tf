# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:09:58 2016
Test MNIST dataset
@author: liudiwei
"""

from sklearn import neighbors
from utils.mnist_utils import DataUtils
import datetime
import numpy as np


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


def classify():
    train_images, train_labels, test_images, test_labels = main()
    start_time = datetime.datetime.now()

    knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(train_images, train_labels)

    start_idx = 4999
    length = 5000
    end_idx = start_idx + length

    predict_label = knn.predict(test_images[start_idx:end_idx])

    end_time = datetime.datetime.now()
    print('use time: ' + str(end_time - start_time))
    print('error rate: ' + str(
        1 - (np.sum(predict_label == test_labels[start_idx:end_idx]) * 1.0 / (end_idx - start_idx))))


if __name__ == "__main__":
    classify()
