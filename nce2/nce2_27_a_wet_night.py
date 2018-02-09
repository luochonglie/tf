#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/08 14:26
# @Author  : c0l0121
# @File    : nce2_27_a_wet_night.py
# @Desc    :


import unittest


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ["A wet night",
                    "What happened to the boys in the night?",
                    "Late in the afternoon, the boys put up their tent in the middle of a field.",
                    "As soon as this was done, they cooked a meal over an open fire.",
                    "They were all hungry and the food smelled good.",
                    "After a wonderful meal, they told stories and sang songs by the campfire.",
                    "But some time later it began to rain.",
                    "The boys felt tired so they put out the fire and crept into their tent.",
                    "Their sleeping bags were warm and comfortable, so they all slept soundly.",
                    "In the middle of the night, two boys woke up and began shouting.",
                    "The tent was full of water!",
                    "They all leapt out of their sleeping bags and hurried outside.",
                    "It was raining heavily and they found that a stream had formed in the field.",
                    "The stream wound its way across the field and then flowed right under their tent!",
                    ]

        actual = ["A wet night",
                  "What happened to the boys in the night?",
                  "Late in the afternoon, the boys put up their tent in the middle of a field.",
                  "As soon as this was done, they cooked a meal over an open fire.",
                  "They were all hungry and the food smelled good.",
                  "After a wonderful meal, they told stories and sang songs by the campfire.",
                  "But some time later it began to rain.",
                  "The boys felt tired so they put out the fire and crept into their tent.",
                  "Their sleeping bags were warm and comfortable, so they all slept soundly.",
                  "In the middle of the night, two boys woke up and began shouting.",
                  "The tent was full of water!",
                  "They all leapt out of their sleeping bags and hurried outside.",
                  "It was raining heavily and they found that a stream had formed in the field.",
                  "The stream wound its way across the field and then flowed right under their tent!"
                  ]

        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i])


if __name__ == '__main__':
    unittest.main()
