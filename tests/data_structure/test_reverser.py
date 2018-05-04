#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/02 14:02
# @Author  : c0l0121
# @File    : test_searcher.py
# @Desc    :


import unittest
import numpy as np
import data_structure.reverser as reverser

array_to_be_process = [None, [], [1], [1, 2], [1, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1],
                       [2, 3, 4, 6, 78, 4, 2, 3, 32, 45, 45, 454, 54, 545, 4, 1, 23, 22, 323]]
array_processed = [None, [], [1], [2, 1], [2, 3, 1], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8],
                   [323, 22, 23, 1, 4, 545, 54, 454, 45, 45, 32, 3, 2, 4, 78, 6, 4, 3, 2]]


class TestReverser(unittest.TestCase):
    def test_quick_sort(self):
        for i in range(len(array_to_be_process)):
            actual_array = reverser.reverse(array_to_be_process[i])
            self.assertEqual(array_processed[i], actual_array)
