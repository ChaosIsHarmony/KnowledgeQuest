'''
FROM "KnowledgeQuest/" directory
RUN $ python3 -m tests.test_entities
'''
import unittest2

from src.modes import QuestGiver as qg

DUMMY_DATA_FILEPATH = "./tests/test_data/dummy_quests.json"

class TestEntities(unittest2.TestCase):

    def test_load_quests(self):
        file_contents = qg.load_quests(DUMMY_DATA_FILEPATH)

        # test number of dummy entries
        self.assertEqual(len(file_contents), 3)
        # test fields have been parsed correctly
        self.assertEqual(file_contents[0]["id"], 1)


    def test_deserialize_quests(self):
        quests = qg.deserialize_quests(qg.load_quests(DUMMY_DATA_FILEPATH))

        # test number o fdummy entries
        self.assertEqual(len(quests), 3)
        # test proper parsing
        self.assertEqual(quests[0].get_id(), 1)


    def test_fetch_quests(self):
        quests = qg.fetch_quests(DUMMY_DATA_FILEPATH)

        # test number o fdummy entries
        self.assertEqual(len(quests), 3)
        # test proper parsing
        self.assertEqual(quests[0].get_id(), 1)


    def test_get_end_date(self):
        now = 1653228559.4072394
        endDate1 = qg.get_end_date(now, 7)
        endDate2 = qg.get_end_date(now, 14)
        endDate4 = qg.get_end_date(now, 28)
        endDate8 = qg.get_end_date(now, 56)

        self.assertEqual(endDate1, "2022-5-29")
        self.assertEqual(endDate2, "2022-6-5")
        self.assertEqual(endDate4, "2022-6-19")
        self.assertEqual(endDate8, "2022-7-17")


if __name__ == "__main__":
    unittest2.main()
