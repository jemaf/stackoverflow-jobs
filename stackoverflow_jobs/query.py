"""
 Created on Mon Apr 22 2019

 Copyright (c) 2019 João Eduardo Montandon
"""

import requests
from .filters import Filter


class Query:

    def __init__(self, timeout=60):
        self.filters = []
        self.timeout = timeout

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

    def execute(self, timeout=None):
        query_timeout = timeout or self.timeout
        url = self.build_query()
        return requests.get(url, timeout=query_timeout).content
