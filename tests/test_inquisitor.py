'''
To test individually:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m tests.test_inquisitor

To test all tests:
FROM "KnowledgeQuest/" directory
RUN $ python3 -m unittest2 discover -s tests/ -p "test*.py"
'''
import unittest2

import src.common as common
from src.modes import Inquisitor as inq

class TestInquisitor(unittest2.TestCase):

    def test_fetch_questions(self):
        questions = inq.fetch_questions(common.TEST_QUESTIONS_FILEPATH)

        self.assertEquals(questions[0].get_id(), 1)
        self.assertEquals(questions[0].get_num_times_asked(), 10)


    def test_create_inquisition(self):
        questions = inq.fetch_questions(common.TEST_QUESTIONS_FILEPATH)
        inquisition = inq.create_inquisition(questions, 5)

        self.assertEquals(len(inquisition), 5)
        for question in inquisition:
            self.assertTrue(question.get_accuracy() < 0.61)

        # impossible num questions
        inquisition = inq.create_inquisition(questions, 100000000)

        self.assertEquals(len(inquisition), len(questions))

        # threshold lower than lowest accuracy, so purely ordered by least recently asked
        # - in this case, all questions have not yet been asked
        inquisition = inq.create_inquisition(questions, 5, 0.0)

        for question in inquisition:
            self.assertTrue(question.get_last_asked() < 1)


    def test_perform_inquisition(self):
        pass


if __name__ == "__main__":
    unittest2.main()
