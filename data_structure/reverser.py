#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/04 9:36
# @Author  : c0l0121
# @File    : reverser.py
# @Desc    :


def reverse(array):
    if array is None or len(array) == 0:
        return array
    else:
        return __reverse(array[:], 0, len(array) - 1)


def __reverse(array, f, l):
    if f < l:
        __exchange(array, f, l)
        __reverse(array, f + 1, l - 1)

    return array


def __exchange(array, x, y):
    t = array[x]
    array[x] = array[y]
    array[y] = t
