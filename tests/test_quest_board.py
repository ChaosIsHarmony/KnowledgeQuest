'''
To test individually:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m tests.test_quest_board

To test all tests:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m unittest2 discover -s tests/ -p "test*.py"
'''
import unittest2
import src.common as common

from src.modes import QuestBoard as qb
from src.enums.CoreStats import CoreStats, coreStatsMap
from src.enums.Skills import Skills, skillsMap

class TestQuestBoard(unittest2.TestCase):

    def test_load_quests(self):
        file_contents = common.load_file(common.QUESTS_FILEPATH)

        # test number of dummy entries
        self.assertEqual(len(file_contents), 3)
        # test fields have been parsed correctly
        self.assertEqual(file_contents[0]["id"], 1)


    def test_deserialize_quests(self):
        quests = qb.deserialize_quests(common.load_file(common.QUESTS_FILEPATH))

        # test number o fdummy entries
        self.assertEqual(len(quests), 3)
        # test proper parsing
        self.assertEqual(quests[0].get_id(), 1)


    def test_fetch_quests(self):
        quests = qb.fetch_quests(common.QUESTS_FILEPATH)

        # test number o fdummy entries
        self.assertEqual(len(quests), 3)
        # test proper parsing
        self.assertEqual(quests[0].get_id(), 1)


    def test_get_end_date(self):
        now = 1653228559.4072394
        endDate1 = qb.get_end_date(now, 7)
        endDate2 = qb.get_end_date(now, 14)
        endDate4 = qb.get_end_date(now, 28)
        endDate8 = qb.get_end_date(now, 56)

        self.assertEqual(endDate1, "2022-5-29")
        self.assertEqual(endDate2, "2022-6-5")
        self.assertEqual(endDate4, "2022-6-19")
        self.assertEqual(endDate8, "2022-7-17")


    def test_create_str_from_list(self):
        coreStats2 = [CoreStats.STRENGTH.value, CoreStats.CHARISMA.value]
        coreStatsAffectedStr2 = qb.create_str_from_list(coreStats2, coreStatsMap)

        self.assertEqual(coreStatsAffectedStr2, "STR, CHA")

        skills2 = [Skills.STAMINA.value, Skills.POWER.value]
        skillsAffected2 = qb.create_str_from_list(skills2, skillsMap)

        self.assertEqual(skillsAffected2, "Physical-Stamina, Physical-Power")


if __name__ == "__main__":
    unittest2.main()
