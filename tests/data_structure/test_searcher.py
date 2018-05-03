#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/02 14:02
# @Author  : c0l0121
# @File    : test_searcher.py
# @Desc    :


import unittest
import data_structure.searcher as searcher


class TestSearcher(unittest.TestCase):
    def test_binary_search(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(2, searcher.binary_search(array, 3))

        array = []
        self.assertEqual(-1, searcher.binary_search(array, 3))

        array = [1]
        self.assertEqual(-1, searcher.binary_search(array, 3))

        array = [1, 2, 3, 4]
        self.assertEqual(1, searcher.binary_search(array, 2))

    def test_binary_search_recursive(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(2, searcher.binary_search_recursive(array, 3))

        array = []
        self.assertEqual(-1, searcher.binary_search_recursive(array, 3))

        array = [1]
        self.assertEqual(-1, searcher.binary_search_recursive(array, 3))

        array = [1, 2, 3, 4]
        self.assertEqual(1, searcher.binary_search_recursive(array, 2))
