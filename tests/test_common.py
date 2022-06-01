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
        fileContents = common.load_file(common.TEST_QUESTS_FILEPATH)

        # test number of dummy entries
        self.assertEqual(len(fileContents), 2)
        # test fields have been parsed correctly
        self.assertEqual(fileContents[0]["id"], 1)


    def test_load_file_questions(self):
        fileContents = common.load_file(common.TEST_QUESTIONS_FILEPATH)

        # test number of dummy entries
        self.assertEqual(len(fileContents), 9)
        # test fields have been parsed correctly
        self.assertEqual(fileContents[0]["id"], 1)


    def test_write_file(self):
        fileContents = common.load_file(common.TEST_QUESTIONS_FILEPATH)
        questions = common.deserialize_questions(fileContents)
        common.write_file(questions, common.TMP_FILEPATH)
        newFileContents = common.load_file(common.TMP_FILEPATH)

        self.assertEqual(fileContents, newFileContents)




if __name__ == "__main__":
    unittest2.main()
