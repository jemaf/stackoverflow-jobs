"""
 Created on Mon Apr 22 2019

 Copyright (c) 2019 João Eduardo Montandon
"""


class Filter:

    def build(self):
        raise NotImplementedError


class Description(Filter):

    def __init__(self, text=""):
        self.text = text

    def build(self):
        tokens = self.text.split(" ")
        return "q={}".format("+".join(tokens))
