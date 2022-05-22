'''
FROM "KnowledgeQuest/" directory
RUN $ python3 -m tests.test_entities
'''
import unittest2

from src.entities.Quest import Quest

class TestEntities(unittest2.TestCase):

    def test_proper_default_instantiation(self):
        quest = Quest()

        self.assertEqual(quest.get_text(), "")
        self.assertEqual(quest.get_difficulty(), 0)

    def test_proper_instantiation(self):
        questText = "This is the text."
        quest = Quest(questText, 10)

        self.assertEqual(quest.get_text(), questText)
        self.assertEqual(quest.get_difficulty(), 10)


if __name__ == "__main__":
    unittest2.main()
