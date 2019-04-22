"""
 Created on Mon Apr 22 2019

 Copyright (c) 2019 João Eduardo Montandon
"""

from unittest import TestCase

from stackoverflow_jobs.src.query import Query
from stackoverflow_jobs.src.filters import Description, Location


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
        self.skipTest("To be implemented")

    def test_queryWithLikedTechs(self):
        self.skipTest("To be implemented")

    def test_queryWithDislikedTechs(self):
        self.skipTest("To be implemented")

    def test_queryWithCompensation(self):
        self.skipTest("To be implemented")

    def test_queryWithCompensationEquity(self):
        self.skipTest("To be implemented")

    def test_queryWithPerks(self):
        self.skipTest("To be implemented")

    def test_queryWithExperienceLevel(self):
        self.skipTest("To be implemented")

    def test_queryWithRoles(self):
        self.skipTest("To be implemented")

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
