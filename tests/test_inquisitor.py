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
        questions = inq.fetch_questions(common.QUESTIONS_FILEPATH)

        self.assertEquals(questions[0].get_id(), 1)






if __name__ == "__main__":
    unittest2.main()
