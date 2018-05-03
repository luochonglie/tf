#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/02 13:40
# @Author  : c0l0121
# @File    : searcher.py
# @Desc    :


def binary_search(array, value):
    """ 查找所给数值在有序数组中的位置，找不到则返回-1

    :param array: 数组
    :param value: 待查找的数值
    :return: 找到则返回数值在数组中的下标，否则返回-1
    """
    ret = -1
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > value:
            end = mid - 1
        elif array[mid] < value:
            start = mid + 1
        else:
            ret = mid
            break
    return ret


def binary_search_recursive(array, value, start=None, end=None):
    """ 查找所给数值在有序数组中的位置，找不到则返回-1

    :param start: 开始位置
    :param end: 结束位置
    :param array: 数组
    :param value: 待查找的数值
    :return: 找到则返回数值在数组中的下标，否则返回-1
    """
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    if start > end:
        return -1

    mid = (start + end) // 2

    if value < array[mid]:
        return binary_search_recursive(array, value, start, mid - 1)
    elif value > array[mid]:
        return binary_search_recursive(array, value, mid + 1, end)
    else:
        return mid