'''
To test individually:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m tests.test_common

To test all tests:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m unittest2 discover -s tests/ -p "test*.py"
'''
import unittest2

import src.common as common

class TestCommon(unittest2.TestCase):

    def test_load_file_quests(self):
        file_contents = common.load_file(common.TEST_QUESTS_FILEPATH)

        # test number of dummy entries
        self.assertEqual(len(file_contents), 3)
        # test fields have been parsed correctly
        self.assertEqual(file_contents[0]["id"], 1)


    def test_load_file_questions(self):
        file_contents = common.load_file(common.TEST_QUESTIONS_FILEPATH)

        # test number of dummy entries
        self.assertEqual(len(file_contents), 9)
        # test fields have been parsed correctly
        self.assertEqual(file_contents[0]["id"], 1)



if __name__ == "__main__":
    unittest2.main()
