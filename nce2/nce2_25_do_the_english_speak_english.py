#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/02 10:56
# @Author  : c0l0121
# @File    : nce2_25_do_the_english_speak_english.py
# @Desc    :


import unittest


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ('Do the English speak English?\n'
                    'Why does the writer not understand the porter?\n'
                    'I arrived in London at last.\n'
                    'The railway station was big, black and dark.\n'
                    'I did not know the way to my hotel, so I asked a porter.\n'
                    'I not only spoke English very carefully, but very clearly as well.\n'
                    'The porter, however, could not understand me.\n'
                    'I repeated my question several times and at last he understood.\n'
                    'He answered me, but he spoke neither slowly nor clearly.\n'
                    '\'I am a foreigner,\' I said.\n'
                    'Then he spoke slowly, but I could not understand him.\n'
                    'My teacher never spoke English like that!\n'
                    'The porter and I looked at each other and smiled.\n'
                    'Then he said something and I understood it.\n'
                    '\'You\'ll soon learn English!\' he said.\n'
                    'I wonder.\n'
                    'In England, each person speaks a different language.\n'
                    'The English understand each other, but I don\'t understand them!\n'
                    'Do they speak English?'
                    )

        actual = ("Do/ the English speak English?\n"
                  "Why does the writer not understand the porter?\n"
                  "I arrived in London at last.\n"
                  "The railway station was big, black and dark.\n"
                  "I did not know the way to my hotel, so I asked a porter.\n"
                  "I not only spoke English very carefully, but very clearly as well.\n"
                  "The porter, however, could not understand me.\n"
                  "I repeated my question several times and at last he understood.\n"
                  "He answered me, but he spoke neither slowly nor clearly.\n"
                  "'I am a foreigner,' I said.\n"
                  "Then he spoke slowly, but I could not understand him.\n"
                  "My teacher never spoke English like that!\n"
                  "The porter and I looked at each other and smiled.\n"
                  "Then he said something and I understood it.\n"
                  "'You'll soon learn English!' he said.\n"
                  "I wonder.\n"
                  "In England, each person speaks a different language.\n"
                  "The English understand each other, but I don't understand them!\n"
                  "Do they speak English?")
        self.maxDiff = None
        self.assertMultiLineEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
