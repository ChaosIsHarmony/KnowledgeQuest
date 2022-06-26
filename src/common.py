import json

from .factories.QuestFactory import QuestFactory
from .factories.QuestionFactory import QuestionFactory
from .interfaces.IQuest import IQuest
from .interfaces.IQuestion import IQuestion
from typing import List, TypeVar

QUESTS_FILEPATH = "./data/quests.json"
TEST_QUESTS_FILEPATH = "./tests/data/test_quests.json"
QUESTIONS_FILEPATH = "./data/questions.json"
TEST_QUESTIONS_FILEPATH = "./tests/data/test_questions.json"
TMP_FILEPATH = "./tests/data/tmp.json"

T = TypeVar("T", IQuest, IQuestion)

def load_file(path: str) -> List[str]:
    contents = []

    try:
        with open(path) as f:
            contents = json.load(f)
    except Exception as e:
        print(f"There was a problem loading the file: {path}\n{e}")

    return contents


def write_file(data, path: str) -> None:
    with open(path, 'w') as f:
        f.write(json.dumps([obj.to_json() for obj in data]))


def compare_questions_by_accuracy(a: IQuestion, b: IQuestion) -> int:
    '''
    Sorts questions in ascending order by accuracy.
    '''
    if a.get_accuracy() > b.get_accuracy():
        return 1
    if a.get_accuracy() < b.get_accuracy():
        return -1
    return 0


def compare_questions_by_last_asked(a: IQuestion, b: IQuestion) -> int:
    '''
    Sorts questions by the last time they were asked.
    Old -> Recent
    '''
    if a.get_last_asked() > b.get_last_asked():
        return 1
    if a.get_last_asked() < b.get_last_asked():
        return -1
    return 0


def deserialize_questions(questionsJson: List[str]) -> List[IQuestion]:
    questions = []

    for question in questionsJson:
        questions.append(QuestionFactory.from_dict(question))

    return questions


def deserialize_quests(questsJson: List[str]) -> List[IQuest]:
    quests = []

    for quest in questsJson:
        quests.append(QuestFactory.from_dict(quest))

    return quests


def get_highest_id(collection: List[T]) -> int:
    highestId = 0
    for item in collection:
        if item.get_id() > highestId:
            highestId = item.get_id()

    return highestId


if __name__ == "__main__":
    contents = load_file(QUESTIONS_FILEPATH)
    questions = deserialize_questions(contents)

    highestId = get_highest_id(questions)
    print(f"The highest question id is: {highestId}")
