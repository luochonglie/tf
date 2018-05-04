#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/03 11:12
# @Author  : c0l0121
# @File    : sorter.py
# @Desc    :


def quick_sort(array):
    """ 快速排序，将数组按从小到大排序

    :param array: 待排序数组
    :return: 有序数组
    """
    copy = __copy_array(array)
    if __is_lte_one(copy):
        return copy
    else:
        __quick_sort(copy)

    return copy


def __quick_sort(array, p=None, r=None):
    """ 快速排序，将数组指定位置的元素按从小到大排序

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


def insert_sort(array):
    copy = __copy_array(array)
    if __is_lte_one(copy):
        return copy
    else:
        for j in range(1, len(copy)):
            i = j - 1
            key = copy[j]
            while i >= 0 and copy[i] > key:
                copy[i + 1] = copy[i]
                i -= 1
            copy[i + 1] = key
        return copy


def shell_sort(array):
    copy = __copy_array(array)


def __is_lte_one(array):
    if array is None or len(array) <= 1:
        return True
    else:
        return False


def __is_empty(array):
    if array is None or len(array) == 0:
        return True
    else:
        return False


def __copy_array(array):
    """复制数组

    :param array: 待复制的数组
    :return: 复制的数组
    """
    if array is None:
        return array
    else:
        return array[:]


def __exchange(array, i, j):
    """交换数组指定位置的两个元素

    :param array: 数组
    :param i: 位置1
    :param j: 位置2
    """
    if i != j:
        x = array[i]
        array[i] = array[j]
        array[j] = x
