#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/08 14:26
# @Author  : c0l0121
# @File    : nce2_27_a_wet_night.py
# @Desc    :


import unittest


class TestStringMethods(unittest.TestCase):
    def test_article(self):
        expected = ["Taxi!",
                    "Does Captain Fawcett think any trip is too dangerous?",
                    "Captain Ben Fawcett has bought an unusual taxi and has begun a new service.",
                    "The 'taxi' is a small Swiss aeroplane called a 'Pilatus Porter'.",
                    "This wonderful plane can carry seven passengers.",
                    "The most surprising thing about it, however, is that it can land anywhere: "
                    "on snow, water, or even on a ploughed field.",
                    "Captain Fawcett's first passenger was a doctor who flew from Birmingham to a lonely village"
                    "in the Welsh mountains.",
                    "Since then, Captain Fawcett haa flown passengers to many unusual places.",
                    "Once he landed on the roof of a block of flats and on another occasion, he landed in a "
                    "deserted car park.",
                    "Captain Fawcett has just refused a strange request from a businessman.",
                    "The man wanted to fly to Rockall, a lonely island in the Atlantic ocean, "
                    "but Captain Fawcett did not take him because trip was too dangerous."
                    ]

        actual = ["No parking",
                  "What is Jasper White's problem?",
                  "Jasper White is one of those rare people who believes in ancient myths.",
                  "He has just bought a new house in the city, but ever since he moved in, "
                  "he has had trouble with cars and their owners.",
                  "When he returns home at night, he always finds that someone has parked a car outside his gate.",
                  "Because of this, he has not been able to get his own car into his garage even once.",
                  "Jasper has put up 'No parking' signs outside his gate, but these have not had any effect.",
                  "Now he has put an ugly stone head over the gate.",
                  "It is one of the ugliest faces I have ever seen.",
                  "I asked him what it was and he told me that it was Medusa the Gorgon.",
                  "Jasper hopes that she will turn cars and their owners to stone.",
                  "But none of them has been turn to stone yet."
                  ]

        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i])


if __name__ == '__main__':
    unittest.main()
