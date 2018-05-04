#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/03 11:12
# @Author  : c0l0121
# @File    : sorter.py
# @Desc    :


def quick_sort(array):
    """ 快速排序，将元素按从小到大排序

    :param array: 待排序数组
    :return: 有序数组
    """

    copied_array = __copy_array(array)
    __quick_sort(copied_array)

    return copied_array


def __copy_array(array):
    """复制数组

    :param array: 待复制的数组
    :return: 复制的数组
    """
    if array is None:
        return None
    else:
        return array[:]


def __quick_sort(array, p=None, r=None):
    """ 快速排序，将元素按从小到大排序

    :param array: 待排序数组
    :param p: 开始位置
    :param r: 结束位置
    :return: 有序数组
    """
    if p is None:
        p = 0

    if r is None:
        r = len(array) - 1

    if p < r:
        q = __partition(array, p, r)
        __quick_sort(array, p, q - 1)
        __quick_sort(array, q + 1, r)


def __partition(array, p, r):
    """将数组分成左右两个分区，左侧比中心点小，右侧比中心点大

    :param array: 待分区数组
    :param p: 开始位置
    :param r: 结束位置
    :return: 中心点
    """
    x = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] <= x:
            i += 1
            __exchange(array, i, j)

    __exchange(array, i + 1, r)
    return i + 1


def __exchange(array, i, j):
    if i != j:
        x = array[i]
        array[i] = array[j]
        array[j] = x
