from unittest import TestCase

from stackoverflow_jobs.src.query import Query


class TestQuery(TestCase):

    def test_queryWithoutParameters(self):
        q = Query()

        self.assertEquals(q.build_query(),
                          "https://stackoverflow.com/jobs/feed")

    def test_queryWithDescription(self):
        self.skipTest("To be implemented")

    def test_queryWithLocation(self):
        self.skipTest("To be implemented")

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
