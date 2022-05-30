import json

from typing import List
from .entities.IQuestion import IQuestion

QUESTS_FILEPATH = "./data/quests.json"
TEST_QUESTS_FILEPATH = "./data/test_quests.json"
QUESTIONS_FILEPATH = "./data/questions.json"
TEST_QUESTIONS_FILEPATH = "./data/test_questions.json"
TMP_FILEPATH = "./data/tmp.json"


def load_file(path: str) -> List[str]:
    contents = []

    try:
        with open(path) as f:
            contents = json.load(f)
    except:
        print(f"There was a problem loading the file: {path}")

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
