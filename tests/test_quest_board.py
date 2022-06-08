'''
To test individually:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m tests.test_quest_board

To test all tests:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m unittest2 discover -s tests/ -p "test*.py"
'''
import io
import sys
import unittest2
import src.common as common

from src.modes import QuestBoard as qb
from src.enums.CoreStats import CoreStats, coreStatsMap
from src.enums.Skills import Skills, skillsMap

class TestQuestBoard(unittest2.TestCase):

    def stub_stdin(testcase_inst, inputs):
        stdin = sys.stdin

        def cleanup():
            sys.stdin = stdin

        testcase_inst.addCleanup(cleanup)
        sys.stdin = io.StringIO(inputs)


    def test_fetch_quests(self):
        quests = qb.fetch_quests(common.TEST_QUESTS_FILEPATH)

        # test number of dummy entries
        self.assertEqual(len(quests), 2)
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

        skills2 = [Skills.STEM.value, Skills.LINGUISTICS.value]
        skillsAffected2 = qb.create_str_from_list(skills2, skillsMap)

        self.assertEqual(skillsAffected2, "STEM, Linguistics")


    def test_quest_requires_update(self):
        quests = qb.fetch_quests(common.TEST_QUESTS_FILEPATH)
        questsNeedUpdate = list(filter(lambda q: qb.quest_requires_update(q), quests))

        self.assertEqual(len(questsNeedUpdate), 1)


    def test_get_target_input(self):
        data_and_answers = [
            ("", "Title: ", "Bobo"),
            (0, "Duration: ", 30)
        ]

        for default, message, userInput in data_and_answers:
            self.stub_stdin(str(userInput))
            value = qb.get_target_input(default, message)

            self.assertEqual(userInput, value)
            self.assertEqual(type(userInput), type(value))



if __name__ == "__main__":
    unittest2.main()
