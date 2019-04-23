"""
 Created on Mon Apr 22 2019

 Copyright (c) 2019 João Eduardo Montandon
"""

import requests
from .filters import Filter


class Query:

    def __init__(self):
        self.filters = []

    def __add__(self, filter):
        if isinstance(filter, Filter):
            self.filters.append(filter)
            return self

        raise RuntimeError("{} is not a filter".format(filter))

    def build_query(self):
        q = "https://stackoverflow.com/jobs/feed"

        if self.filters != []:
            q += "?" + "&".join([f.build() for f in self.filters])
        return q

    def execute(self):
        url = self.build_query()
        return requests.get(url).content
