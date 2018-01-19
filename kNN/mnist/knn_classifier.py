# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:09:58 2016
Test MNIST dataset
@author: liudiwei
"""

from sklearn import neighbors
from utils.mnist_utils import DataUtils
import datetime


def classify():
    train_image, train_lable, test_image, test_label = main()
    start_time = datetime.datetime.now()

    knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(train_image, train_lable)

    start_idx = 0
    end_idx = 10

    predict_label = knn.predict(test_image[start_idx:end_idx])
    matched = predict_label == test_label[start_idx:end_idx]

    end_time = datetime.datetime.now()
    print('use time: ' + str(end_time - start_time))
    print('error rate: ' + str(1 - (list(matched).count(True) * 1.0 / (end_idx - start_idx))))

def main():
    start_time = datetime.datetime.now()

    training_image = '../../dataset/MNIST/train-images.idx3-ubyte'
    training_label = '../../dataset/MNIST/train-labels.idx1-ubyte'
    testfile_image = '../../dataset/MNIST/t10k-images.idx3-ubyte'
    testfile_label = '../../dataset/MNIST/t10k-labels.idx1-ubyte'
    train_image = DataUtils(filename=training_image).getImage()
    train_label = DataUtils(filename=training_label).getLabel()
    test_image = DataUtils(testfile_image).getImage()
    test_label = DataUtils(testfile_label).getLabel()

    end_time = datetime.datetime.now()
    print('Load data use time: ' + str(end_time - start_time))

    return train_image, train_label, test_image, test_label


if __name__ == "__main__":
    classify()
