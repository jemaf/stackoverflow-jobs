"""
 Created on Mon Apr 22 2019

 Copyright (c) 2019 João Eduardo Montandon
"""

from unittest import TestCase

from stackoverflow_jobs.src.query import Query
from stackoverflow_jobs.src.filters import (Description, Location, Remote,
                                            Technologies, Salary, Equity,
                                            ExperienceLevel, Role)


class TestQuery(TestCase):

    def test_queryWithoutParameters(self):
        q = Query()
        self.assertEquals(q.build_query(),
                          "https://stackoverflow.com/jobs/feed")

    def test_queryWithDescription(self):
        q = Query() + Description("Example Description")

        self.assertIn("q=Example+Description", q.build_query())

    def test_queryWithLocation(self):
        q = Query() + Location("San Francisco")
        self.assertIn("l=San+Francisco&u=Km&d=20", q.build_query())

    def test_queryWithRemoteFlag(self):
        q = Query() + Remote()
        self.assertIn("r=true", q.build_query())

    def test_queryWithLikedTechs(self):
        liked_techs = ["html", "c#", "java"]
        q = Query() + Technologies(liked=liked_techs)
        self.assertIn("tl=html+c#+java", q.build_query())

    def test_queryWithDislikedTechs(self):
        disliked_techs = ["php", "regex", "objective-c"]
        q = Query() + Technologies(disliked=disliked_techs)
        self.assertIn("td=php+regex+objective-c", q.build_query())

    def test_queryWithLikedAndDislikedTechs(self):
        liked_techs = ["html", "c#", "java"]
        disliked_techs = ["php", "regex", "objective-c"]

        q = Query() + Technologies(liked=liked_techs, disliked=disliked_techs)
        self.assertIn("tl=html+c#+java&td=php+regex+objective-c",
                      q.build_query())

    def test_queryWithMonetaryCompensation(self):
        q = Query() + Salary(8880, Salary.Coin.BRL)
        self.assertIn("s=8880&c=BRL", q.build_query())

    def test_queryWithEquityCompensation(self):
        q = Query() + Equity()
        self.assertIn("e=true", q.build_query())

    def test_queryWithPerks(self):
        self.skipTest("To be implemented")

    def test_queryWithExperienceLevel(self):
        q = Query() + ExperienceLevel(ExperienceLevel.Level.STUDENT,
                                      ExperienceLevel.Level.SENIOR)
        self.assertIn("c=brl&ms=Student&mxs=Senior", q.build_query())

    def test_queryWithRoles(self):
        roles = [Role.Type.BACKEND, Role.Type.FRONTEND]
        q = Query() + Role(roles)
        self.assertIn("dr=BackendDeveloper&dr=FrontendDeveloper",
                      q.build_query())

    def test_queryCannotHaveMoreThanFiveRoles(self):
        roles = [Role.Type.BACKEND, Role.Type.FRONTEND, Role.Type.DATABASE,
                 Role.Type.DESIGN, Role.Type.EMBEDDED, Role.Type.GAME]
        self.assertRaiss(RuntimeError, Role, roles)

    def test_queryWithJobType(self):
        self.skipTest("To be implemented")

    def test_queryWithJobFeatures(self):
        self.skipTest("To be implemented")

    def test_queryWithCompaniesToInclude(self):
        self.skipTest("To be implemented")

    def test_queryWithCompaniesToExclude(self):
        self.skipTest("To be implemented")

    def test_queryWithIndustryType(self):
        self.skipTest("To be implemented")
