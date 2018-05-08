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


def insertion_sort(array):
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
    if __is_lte_one(copy):
        return copy
    else:
        length = len(copy)
        gap = 1
        while gap < length // 3:
            gap = gap * 3 + 1

        while gap > 0:
            for j in range(gap, length):
                key = copy[j]
                i = j - gap
                while i >= 0 and copy[i] > key:
                    copy[i + gap] = copy[i]
                    i -= gap
                copy[i + gap] = key
            gap //= 3

        return copy


def merge_sort_recursion(array):
    copy = __copy_array(array)
    if __is_lte_one(copy):
        return copy
    else:
        __merge_sort_recursion(copy, 0, len(copy) - 1)
        return copy


def __merge_sort_recursion(array, left, right):
    if left < right:
        mid = (left + right) // 2
        __merge_sort_recursion(array, left, mid)
        __merge_sort_recursion(array, mid + 1, right)
        __merge_sentry(array, left, mid, right)


def __merge_sentry(array, left, mid, right):
    left_array = []
    right_array = []

    left_array.extend(array[left:(mid + 1)])
    left_array.append(float('inf'))

    right_array.extend(array[(mid + 1):(right + 1)])
    right_array.append(float('inf'))

    i = 0
    j = 0
    for k in range(left, right + 1):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1


def __merge(array, left, mid, right):
    tmp_array = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if array[i] <= array[j]:
            tmp_array.append(array[i])
            i += 1
        else:
            tmp_array.append(array[j])
            j += 1

    if i <= mid:
        tmp_array.extend(array[i:mid + 1])

    if j <= right:
        tmp_array.extend(array[j:right + 1])

    for k in range(left, right + 1):
        array[k] = tmp_array[k - left]


def merge_sort_iteration(array):
    copy = __copy_array(array)
    if __is_lte_one(copy):
        return copy
    else:
        __merge_sort_iteration(copy)
        return copy


def __merge_sort_iteration(array):
    sub_grp_len = 1
    length = len(array)
    while sub_grp_len < length:
        left = 0
        while left + sub_grp_len < length:
            mid = left + sub_grp_len - 1
            right = mid + sub_grp_len if mid + sub_grp_len <= length - 1 else length - 1
            __merge(array, left, mid, right)
            left = right + 1
        sub_grp_len *= 2


def selection_sort(array):
    copy = __copy_array(array)
    if __is_lte_one(copy):
        return copy
    else:
        for i in range(0, len(copy)):
            minimal = copy[i]
            minimal_idx = i
            for j in range(i, len(copy)):
                if minimal > copy[j]:
                    minimal = copy[j]
                    minimal_idx = j
            __exchange(copy, i, minimal_idx)
    return copy


def heap_sort(array):
    copy = __copy_array(array)
    if __is_lte_one(copy):
        return copy
    else:
        __heap_sort(copy)
        return copy


def __parent(i):
    return (i - 1) >> 1


def __left(i):
    return (i << 1) + 1


def __right(i):
    return (i << 1) + 2


def __max_heapify(array, i, size):
    l = __left(i)
    r = __right(i)
    largest = i
    if l < size and array[l] > array[largest]:
        largest = l
    if r < size and array[r] > array[largest]:
        largest = r
    if largest != i:
        __exchange(array, largest, i)
        __max_heapify(array, largest, size)


def __build_max_heap(array):
    size = len(array)
    for i in range(__parent(size - 1), -1, -1):
        __max_heapify(array, i, size)


def __heap_sort(array):
    __build_max_heap(array)
    for size in range(len(array), 1, -1):
        __exchange(array, (size - 1), 0)
        __max_heapify(array, 0, size - 1)


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
