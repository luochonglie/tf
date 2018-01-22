# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:09:58 2016
使用 openCV 读取、复制、保存图片
@author: chonglie
"""

import cv2


def read_img(file_name='../dataset/img/cover.jpg'):
    """读取图片

    :param file_name: 图片文件路径，默认'../dataset/img/cover.jpg'

    :return: 图片文件
    """
    return cv2.imread(file_name, 1)


def copy(source):
    """ 复制图片

        :param source: 源图片

        :return: 图片的副本
    """
    if source is not None:
        return source.copy()
    else:
        return None


def show_img(img):
    """显示图片

        :param
            img:图片

    """
    cv2.namedWindow('win')
    cv2.imshow('win', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save(img, file_name='../dataset/img/copy_of_cover.jpg', params=None):
    """保存图片

    :param

        img:图片
        file_name:保存路径及文件名

    :return:
    """
    if (file_name is not None) and (img is not None):
        cv2.imwrite(file_name, img, params)


def save_img_in_low_quality(img, file_name='../dataset/img/copy_of_cover.jpg'):
    save(img, file_name, [int(cv2.IMWRITE_JPEG_QUALITY), 5])


def main():
    img = read_img()
    copy_of_img = copy(img)
    save_img_in_low_quality(copy_of_img)


if __name__ == "__main__":
    main()
