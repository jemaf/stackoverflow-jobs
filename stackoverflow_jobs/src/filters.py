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


class Technologies(Filter):

    def __init__(self, liked=[], disliked=[]):
        self.liked = liked
        self.disliked = disliked

    def build(self):
        queries = []

        if self.liked != []:
            liked_techs = "+".join(self.liked)
            queries.append("tl={}".format(liked_techs))
        if self.disliked != []:
            disliked_techs = "+".join(self.disliked)
            queries.append("td={}".format(disliked_techs))

        return "&".join(queries)


class Salary(Filter):

    class Coin(Enum):
        BRL = "BRL"
        USD = "USD"
        EUR = "EUR"
        GBP = "GBP"
        CAD = "CAD"
        AUD = "AUD"
        INR = "INR"
        SEK = "SEK"
        PLN = "PLN"
        CHF = "CHF"
        DKK = "DKK"
        NZD = "NZD"

    def __init__(self, salary, coin):
        self.salary = salary
        self.coin = coin

    def build(self):
        return "s={}&c={}".format(self.salary, self.coin.value)


class Equity(Filter):

    def build(self):
        return "e=true"


class ExperienceLevel(Filter):

    class Level(Enum):
        STUDENT = "Student"
        JUNIOR = "Junior"
        MIDLEVEL = "MidLevel"
        SENIOR = "Senior"
        LEAD = "Lead"
        MANAGER = "Manager"

    def __init__(self, min_level=None, max_level=None):
        self.min = min_level
        self.max = max_level

    def build(self):
        query_tokens = ["c=brl"]
        if self.min:
            query_tokens.append("ms={}".format(self.min.value))
        if self.max:
            query_tokens.append("mxs={}".format(self.max.value))
        return "&".join(query_tokens)


class Role(Filter):

    class Type(Enum):
        BACKEND = "BackendDeveloper"
        DATABASE = "DatabaseAdministrator"
        DATASCIENCE = "DataScientist"
        DESIGN = "Designer"
        DESKTOP = "DesktopDeveloper"
        DEVOPS = "DevOpsDeveloper"
        EMBEDDED = "EmbeddedDeveloper"
        FRONTEND = "FrontendDeveloper"
        FULLSTACK = "FullStackDeveloper"
        GAME = "GameDeveloper"
        MOBILE = "MobileDeveloper"
        PRODUCT = "ProductManager"
        SYSADMIN = "SystemAdministrator"
        TEST = "QATestDeveloper"

    def __init__(self, roles):
        if len(roles) > 5:
            raise RuntimeError("Query supports five roles at most")
        self.roles = roles

    def build(self):
        query_tokens = ["dr={}".format(r.value) for r in self.roles]
        return "&".join(query_tokens)


class JobType(Filter):

    class Type(Enum):
        PERMANENT = "permanent"
        CONTRACT = "contract"
        INTERNSHIP = "internship"

    def __init__(self, types):
        self.types = types

    def build(self):
        query_tokens = ["j={}".format(t.value) for t in self.types]
        return "&".join(query_tokens)
