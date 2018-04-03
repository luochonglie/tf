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
        expected = ["A private conversation",
                    "Why did the writer complain to the people behind him?",
                    "Last week I went to the theatre.",
                    "I had a very good seat.",
                    "The play was very interesting.",
                    "I did not enjoy it.",
                    "A young man and a young woman were sitting behind me.",
                    "They were talking loudly.",
                    "I got very angry.",
                    "I could not hear the actors.",
                    "I turned round.",
                    "I looked at the man and the woman angrily.",
                    "They did not pay any attention.",
                    "In the end, I could not bear it.",
                    "I turned round again.",
                    "'I can't hear a word,' I said angrily.",
                    "'It's none of your business,' the young man said rudely.",
                    "'This is a private conversation!'"
                    ]

        actual = ["A private conversation",
                  "Why did the writer complain to the people behind him?",
                  "Last week I went to the theatre.",
                  "I had a very good seat.",
                  "The play was very interesting.",
                  "I did not enjoy it.",
                  "A young man and a young woman were sitting behind me.",
                  "They were talking loudly.",
                  "I got very angry.",
                  "I could not hear the actors.",
                  "I turned round.",
                  "I looked at the man and the woman angrily.",
                  "They did not pay any attention.",
                  "In the end, I could not bear it.",
                  "I turned round again.",
                  "'I can't hear a word,' I said angrily.",
                  "'It's none of your business,' the young man said rudely.",
                  "'This is a private conversation!'"
                  ]

        print("The similarity of two strings : %.2f%%" % (lvst.ratio("".join(expected), "".join(actual)) * 100))

        self.maxDiff = None
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
