#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/08 14:26
# @Author  : c0l0121
# @File    : nce2_27_a_wet_night.py
# @Desc    :


import unittest
import Levenshtein as lvst
import os
import nce2.similarity_service as ss


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ["Out of the darkness",
                    "Why was the girl in hospital?",
                    "Nearly a week passed before the girl was able to explain what had happened to her.",
                    "One afternoon she set out from the coast in a small boat and was caught in a storm.",
                    "Towards evening, the boat struck a rock and the girl jumped into the sea.",
                    "Then she swam to the shore after spending the whole night in the water.",
                    "During that time she covered a distance of eight miles.",
                    "Early next morning, she saw a light ahead.",
                    "She knew she was near the shore because the light was high up on the cliffs.",
                    "On arriving at the shore, the girl struggled up the cliff towards the light she had seen.",
                    "That was all she remembered.",
                    "When she woke up a day later, she found herself in hospital."
                    ]

        actual = ["Out of the darkness",
                  "Why was the girl in hospital.",
                  ""
                  ]

        __similarity = lvst.ratio("".join(expected), "".join(actual))
        similarity = ss.Similarity(os.path.basename(__file__), __similarity)

        print("The similarity of these articles : %.2f%%" % (__similarity * 100))
        ss.insert(similarity)
        self.maxDiff = None
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
