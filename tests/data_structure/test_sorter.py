#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/02 14:02
# @Author  : c0l0121
# @File    : test_searcher.py
# @Desc    :


import unittest
import numpy as np
import data_structure.sorter as sorter

array_to_be_sort = [None, [], [1], [1, 2], [2, 2, 2], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
                    [2, 3, 4, 6, 78, 4, 2, 3, 32, 45, 45, 454, 54, 545, 4, 1, 23, 22, 323]]
array_sorted = [None, [], [1], [1, 2], [2, 2, 2], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8],
                [1, 2, 2, 3, 3, 4, 4, 4, 6, 22, 23, 32, 45, 45, 54, 78, 323, 454, 545]]

func_list = ["quick_sort", "insertion_sort", "shell_sort", "merge_sort_recursion", "selection_sort", "heap_sort",
             "counting_sort"]


class TestSorter(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        array_to_be_sort.append(list(np.random.randint(0, 1000, 10000)))
        array_sorted.append(list(np.sort(array_to_be_sort[-1])))
        pass

    # 退出清理工作
    def tearDown(self):
        pass

    def test_quick_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.quick_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_insert_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.insertion_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_shell_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.shell_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_merge_sort_recursion(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.merge_sort_recursion(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_merge_sort_iteration(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.merge_sort_iteration(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_selection_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.selection_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_heap_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.heap_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_counting_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.counting_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_radix_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.radix_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_bucket_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.bucket_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_np_sort(self):
        for i in range(2, len(array_to_be_sort)):
            actual_array = list(np.sort(array_to_be_sort[i]))
            self.assertEqual(array_sorted[i], actual_array,
                             "Failed to sort array. A[%s] = %s." % (i, array_to_be_sort[i]))

    def test_all(self):
        for func in func_list:
            for i in range(len(array_to_be_sort)):
                actual_array = eval('sorter.%s' % func)(array_to_be_sort[i])
                self.assertEqual(array_sorted[i], actual_array,
                                 "Failed to use [%s] to sort array. A[%s] = %s" % (func, i, array_to_be_sort[i]))
