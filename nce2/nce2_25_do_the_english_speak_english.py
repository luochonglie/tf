#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/02 10:56
# @Author  : c0l0121
# @File    : nce2_25_do_the_english_speak_english.py
# @Desc    :


import unittest
import Levenshtein as lvst


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ["Do the English speak English?",
                    "Why does the writer not understand the porter?",
                    "I arrived in London at last.",
                    "The railway station was big, black and dark.",
                    "I did not know the way to my hotel, so I asked a porter.",
                    "I not only spoke English very carefully, but very clearly as well.",
                    "The porter, however, could not understand me.",
                    "I repeated my question several times and at last he understood.",
                    "He answered me, but he spoke neither slowly nor clearly.",
                    "'I am a foreigner,' I said.",
                    "Then he spoke slowly, but I could not understand him.",
                    "My teacher never spoke English like that!",
                    "The porter and I looked at each other and smiled.",
                    "Then he said something and I understood it.",
                    "'You'll soon learn English!' he said.",
                    "I wonder.",
                    "In England, each person speaks a different language.",
                    "The English understand each other, but I don't understand them!",
                    "Do they speak English?"
                    ]

        actual = ["Do the English speak English?",
                  "Why does the writer not understand the porter?",
                  "I arrived in London at last.",
                  "The railway station was big, black and dark.",
                  "I did not know the way to my hotel, so I asked a porter.",
                  "I not only spoke English very carefully, but very clearly as well.",
                  "The porter, however, could not understand me.",
                  "I repeated my question several times and at last he understood.",
                  "He answered me, but he spoke neither slowly nor clearly.",
                  "'I am a foreigner,' I said.",
                  "Then he spoke slowly, but I could not understand him.",
                  "My teacher never spoke English like that!",
                  "The porter and I looked at each other and smiled.",
                  "Then he said something and I understood it.",
                  "'You'll soon learn English!' he said.",
                  "I wonder.",
                  "In England, each person speaks a different language.",
                  "The English understand each other, but I don't understand them!",
                  "Do they speak English?"
                  ]

        print("Similarity between two string : %.2f%%" % (lvst.ratio("".join(expected), "".join(actual)) * 100))

        self.maxDiff = None
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
