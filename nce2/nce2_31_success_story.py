#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/08 14:26
# @Author  : c0l0121
# @File    : nce2_27_a_wet_night.py
# @Desc    :


import unittest
import Levenshtein as lvst


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ["Success Story",
                    "What was Frank's first job?",
                    "Yesterday afternoon Frank Hawkins was telling me about his experiences as young man.",
                    "Before he retired, he was the head of a very large business company, "
                    "but as a boy he used to work in a small shop."
                    "It was his job to repair bicycles and at that time he used to work for fourteen hours a day.",
                    "He save money for years and in 1958 he bought a small workshop for his own.",
                    "In his twenties Frank used to make spare parts for aeroplanes.",
                    "At that time he had two helpers.",
                    "In a few years his small workshop had become a big factory which employed seven hundred and "
                    "twenty-eight people.",
                    "Frank smiled when he remembered his hard early years and the long road to success.",
                    "He was still smiling when the door opened and his wife came in.",
                    "She wanted him to repair their grandson's bicycle."
                    ]

        actual = []

        print("The similarity of two strings : %.2f%%" % (lvst.ratio("".join(expected), "".join(actual)) * 100))

        self.maxDiff = None
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
