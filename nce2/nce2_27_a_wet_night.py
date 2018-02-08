#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/08 14:26
# @Author  : c0l0121
# @File    : nce2_27_a_wet_night.py
# @Desc    :


import unittest


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ("A wet night\n"
                    "What happened to the boys in the night?\n"
                    "Late in the afternoon, the boys put up their tent in the middle of a field.\n"
                    "As soon as this was done, they cooked a meal over an open fire.\n"
                    "They were all hungry and the food smelled good.\n"
                    "After a wonderful meal, they told stories and sang songs by the campfire.\n"
                    "But some time later it began to rain.\n"
                    "The boys felt tired so they put out the fire and crept into their tent.\n"
                    "Their sleeping bag were warn and comfortable, so they all slept soundly.\n"
                    "In the middle of the night, two boys woke up and began shouting.\n"
                    "The tent was full of water!\n"
                    "They all leapt out of their sleeping bags and hurried outside.\n"
                    "It was raining heavily and they found that a stream had formed in the field.\n"
                    "The stream wound its way across the field and then flowed right under their tent!"
                    )

        actual = (" The best art critics\n"
                  "Who is the student's best critic?\n"
                  "I am an art student and I paint a lot of pictures.\n"
                  "Many people pretend that they understand modern art.\n"
                  "They always tell you what a picture is 'about'.\n"
                  "Of course, many pictures are not 'about' anything.\n"
                  "They are just pretty patterns.\n"
                  "We like them in the same way that we like pretty curtain material.\n"
                  "I think that young children often appreciate modern pictures better than anyone else.\n"
                  "They notice more.\n"
                  "My sister is only seven, but she always tells me whether my pictures are good or not.\n"
                  "She came into my room yesterday.\n"
                  "'What are you doing?' she asked.\n"
                  "'I'm hanging this picture on the wall,' I answered, 'It's a new one. Do you like it?'\n"
                  "She looked at it critically for a moment.\n"
                  "'It's all right,' she said, 'but isn't it upside down?'\n"
                  "I looked at it again.\n"
                  "She was right! It was!")
        self.maxDiff = None
        self.assertMultiLineEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
