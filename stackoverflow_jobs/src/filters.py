"""
 Created on Mon Apr 22 2019

 Copyright (c) 2019 João Eduardo Montandon
"""

from enum import Enum, auto


class Filter:

    def build(self):
        raise NotImplementedError


class Description(Filter):

    def __init__(self, text=""):
        self.text = text

    def build(self):
        query_text = self.text.replace(" ", "+")
        return "q={}".format(query_text)


class Location(Filter):

    class Range(Enum):
        FIVE = 5
        TEN = 10
        TWENTY = 20
        FIFITY = 50
        ONEHUNDRED = 100

    def __init__(self, text="", distance=Range.TWENTY):
        self.text = text
        self.range = distance

    def build(self):
        query_text = self.text.replace(" ", "+")

        return "l={}&u=Km&d={}".format(query_text, self.range.value)


class Remote(Filter):

    def build(self):
        return "r=true"
