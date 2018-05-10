#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/03 11:12
# @Author  : c0l0121
# @File    : sorter.py
# @Desc    :


import numpy as np


def quick_sort(array):
    """ 快速排序，将数组按从小到大排序

    :param array: 待排序数组
    :return: 有序数组
    """
    copy = __copy_array(array)
    if __is_no_need_to_sort(copy):
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
    if __is_no_need_to_sort(copy):
        return copy
    else:
        __insertion_sort(copy)
        return copy


def __insertion_sort(array):
    for j in range(1, len(array)):
        i = j - 1
        key = array[j]
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key


def shell_sort(array):
    copy = __copy_array(array)
    if __is_no_need_to_sort(copy):
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
    if __is_no_need_to_sort(copy):
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
    if __is_no_need_to_sort(copy):
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
    if __is_no_need_to_sort(copy):
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
    if __is_no_need_to_sort(copy):
        return copy
    else:
        __heap_sort(copy)
        return copy


def __parent(i):
    return (i - 1) // 2


def __left(i):
    return (i * 2) + 1


def __right(i):
    return (i * 2) + 2


def __heap_sort(array):
    __build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        __exchange(array, 0, i)
        __max_heapify(array, 0, i)


def __build_max_heap(array):
    size = len(array)
    for i in range(__parent(size - 1), -1, -1):
        __max_heapify(array, i, size)


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


def counting_sort(array):
    copy = __copy_array(array)
    if __is_no_need_to_sort(copy):
        return copy
    else:
        __counting_sort(copy, max(array))
        return copy


def __counting_sort(array, max_num):
    c = list(np.zeros(max_num + 1, dtype=np.int16))

    for i in range(0, len(array)):
        c[array[i]] += 1

    for i in range(1, len(c)):
        c[i] += c[i - 1]

    b = array[:]
    for i in range(len(array) - 1, -1, -1):
        array[c[b[i]] - 1] = b[i]
        c[b[i]] -= 1


ARRAY_RADIX_10 = [1, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000,
                  1000000000, 10000000000, 100000000000]


def radix_sort(array):
    copy = __copy_array(array)
    if __is_no_need_to_sort(copy):
        return copy
    else:
        __radix_sort(copy)
        return copy


def __radix_sort(array):
    max_one = max(array)
    d = __get_total_digits(max_one)
    for i in range(1, d + 1):
        __radix_counting_sort(array, i)


def __radix_counting_sort(array, d):
    """对指定位进行计数排序

    :param array: 正整数数组
    :param d: 第n位
    :return: 按指定位排好序的数组
    """
    c = list(np.zeros(10, dtype=np.int16))

    for i in range(len(array)):
        c[__get_digit(array[i], d)] += 1

    for i in range(1, len(c)):
        c[i] += c[i - 1]

    b = array[:]
    for i in range(len(array) - 1, -1, -1):
        array[c[__get_digit(b[i], d)] - 1] = b[i]
        c[__get_digit(b[i], d)] -= 1


def __get_total_digits(num):
    """获取正整数的位数

    :param num: 正整数
    :return: 位数
    """
    i = 2
    while num // ARRAY_RADIX_10[i] != 0:
        i += 1
    return i - 1


def __get_digit(num, d):
    """获取正整数某一位上的数字

    :param num: 正整数
    :param d: 第d位
    :return: 第d位上的数字
    """
    return (num // ARRAY_RADIX_10[d]) % 10


def bucket_sort(array):
    copy = __copy_array(array)
    if __is_no_need_to_sort(copy):
        return copy
    else:
        __bucket_sort(copy)
        return copy


def __bucket_sort(array):
    """用桶排序算法对数组进行从小到大排序

    :param array: 待排序数组
    :return: 已排序数组
    """
    # 数组长度的位数
    digits_of_len = __get_total_digits(len(array))
    # 最大值的位数
    digits_of_max = __get_total_digits(max(array))
    # 桶大小的位数 = 数组长度的位数-1 <=  最大值的位数 + 1
    digits_of_buckets = digits_of_len if digits_of_len <= digits_of_max + 1 else digits_of_max + 1
    # 桶大小
    # len < max : 10^digits(len)
    # len > max : 10^digits(max + 1)
    buckets_size = ARRAY_RADIX_10[digits_of_buckets]
    # 映射到桶内需要去掉几位数 如：348 映射到 10 个桶，需要抹掉2位尾数，因此需要将 348 // 100
    truncate = ARRAY_RADIX_10[digits_of_max + 1] // ARRAY_RADIX_10[digits_of_buckets]

    buckets = [None] * buckets_size
    for i in range(len(buckets)):
        buckets[i] = []

    for i in range(len(array)):
        buckets[__map_to_bucket(array[i], truncate)].append(array[i])

    for i in range(len(buckets)):
        __insertion_sort(buckets[i])

    array.clear()
    for i in range(len(buckets)):
        array.extend(buckets[i])


def __map_to_bucket(num, truncate):
    return num // truncate


def __is_no_need_to_sort(array):
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
