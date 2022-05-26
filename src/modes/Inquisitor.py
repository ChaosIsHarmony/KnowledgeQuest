import json

from .. import common
from ..entities.Question import Question
from typing import List


def deserialize_questions(questionsJson: List[str]) -> List[Question]:
    questions = []

    for question in questionsJson:
        questions.append(Question.from_dict(question))

    return questions


def fetch_questions(path: str) -> List[str]:
    questionsFileContents = common.load_file(common.QUESTIONS_FILEPATH)
    questions = deserialize_questions(questionsFileContents)

    return questions




def run() -> None:
    print("Inquisitor Ran.")
