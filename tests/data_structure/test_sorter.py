#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/02 14:02
# @Author  : c0l0121
# @File    : test_searcher.py
# @Desc    :


import unittest
import numpy as np
import data_structure.sorter as sorter

array_to_be_sort = [[], [1], [1, 2], [1, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
                    [2, 3, 4, 6, 78, 4, 2, 3, 32, 45, 45, 454, 54, 545, 4, 1, 23, 22, 323]]
array_sorted = [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8],
                [1, 2, 2, 3, 3, 4, 4, 4, 6, 22, 23, 32, 45, 45, 54, 78, 323, 454, 545]]


class TestSorter(unittest.TestCase):
    def test_quick_sort(self):
        for i in range(len(array_to_be_sort)):
            actual_array = sorter.quick_sort(array_to_be_sort[i])
            self.assertEqual(array_sorted[i], actual_array)

        actual_array = list(np.random.randint(0, 1000, 100))
        expect_array = list(np.sort(actual_array))
        actual_array = sorter.quick_sort(actual_array)
        self.assertEqual(expect_array, actual_array)
