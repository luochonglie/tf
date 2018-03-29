#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/08 14:26
# @Author  : c0l0121
# @File    : nce2_27_a_wet_night.py
# @Desc    :


import unittest


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ["Football or polo?",
                    "What happened to the man in the boat?",
                    "The Wayle is a small river that cuts across the park near my home.",
                    "I like sitting by the Wayle on fine afternoons.",
                    "It was warm last Sunday, so I went and sat on the river bank as usual.",
                    "Some children were playing games on the bank and there were some people rowing on the river.",
                    "Suddenly, one of the children kicked a ball very hard and it went towards a passing boat.",
                    "Some people on the bank called out to the man in the boat, but he did not hear them.",
                    "The ball struck him so hard that he nearly fell into the water.",
                    "I turned to look at the children, but there weren't any in sight: they had all run away!",
                    "The man laughed when he realized what had happened.",
                    "He called out to the children and threw the ball back to the bank."
                    ]

        actual = ["Football or polo?",
                  "What happened to the man in the boat?",
                  "The Wayle is a small river that cuts across the park near my home.",
                  "I like sitting by the Wayle on fine afternoons.",
                  "It was warm last Sunday, so I went and sat on the river bank as usual.",
                  "Some children were playing games on the bank and there were some people rowing on the river.",
                  "Suddenly, one of the children kicked a ball very hard and it went towards a passing boat.",
                  "Some people on the bank called out to the man in the boat, but he did not hear them.",
                  "The ball struck him so hard that he nearly fell into the water.",
                  "I turned to look at the children, but there weren't any in sight: they had all run away!",
                  "The man laughed when he realized what had happened.",
                  "He called out to the children and threw the ball back to the bank."
                  ]

        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i])


if __name__ == '__main__':
    unittest.main()
