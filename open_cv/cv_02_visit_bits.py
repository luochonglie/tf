# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:09:58 2016
按位操作图片
@author: chonglie
"""
import cv2
import numpy as np
from open_cv import cv_01_read_copy_write as img_utils


def salt(img, num):
    """在图片上加入白色的噪点

    :param img: 图片
    :param num: 噪点数量
    :return: 增加噪点后的图片
    """
    print(img.shape)
    for i in range(num):
        y = int(np.random.random() * img.shape[0])
        x = int(np.random.random() * img.shape[1])
        print("x =", x, "y =", y)

        if img.ndim == 2:
            img[y, x] = 255
        elif img.ndim == 3:
            img[y, x, 0] = 255
            img[y, x, 1] = 255
            img[y, x, 2] = 255
    return img


def split_channel(img):
    """

    :param img: 图片
    :return: 分离后的通道
        red: 红
        green: 绿
        blue: 蓝
    """
    blue, green, red = cv2.split(img)
    return red, green, blue


def show_add_silt():
    img = img_utils.read_img()
    salt_image = salt(img, 500)
    cv2.imshow("Salt", salt_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_split_channel():
    img = img_utils.read_img()
    r, g, b = split_channel(img)
    cv2.imshow("Blue", r)
    cv2.imshow("Red", g)
    cv2.imshow("Green", b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_split_channel()
