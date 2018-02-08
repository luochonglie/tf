#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/02 10:56
# @Author  : c0l0121
# @File    : nce2_25_do_the_english_speak_english.py
# @Desc    :


import unittest


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ("The best art critics\n"
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
                    "She was right! It was!"
                    )

        actual = ("The best art critics\n"
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
