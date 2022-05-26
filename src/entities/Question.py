import time

from ..enums.Skills import Skills
from .IQuestion import IQuestion
from typing import Dict, List


class Question(IQuestion):

    def __init__(self, idNum: int, question_text: str, answers: List[str], n_times_asked: int, n_times_correctly_answered: int, last_asked: time, skills: List[Skills], tags: List[str]):
        self.__id = idNum
        self.__question_text = question_text
        self.__answers = answers
        self.__n_times_asked = n_times_asked
        self.__n_times_answered_correctly = n_times_correctly_answered
        self.__last_date_asked = last_asked
        self.__skills = skills
        self.__tags = tags

    @classmethod
    def from_dict(cls, attrDict) -> IQuestion:
        return cls(attrDict["id"], attrDict["question_text"], attrDict["answers"], attrDict["n_times_asked"], attrDict["n_times_correctly_answered"], attrDict["last_asked"], attrDict["skills"], attrDict["tags"])

    def get_id(self) -> int:
        return self.__id

    def get_question_text(self) -> str:
        return self.__question_text

    def get_question_answers(self) -> List[str]:
        return self.__answers

    def get_num_times_asked(self) -> int:
        return self.__n_times_asked

    def increment_num_times_asked(self) -> None:
        self.__n_times_asked = self.__n_times_asked + 1

    def get_num_times_answered_correctly(self) -> int:
        return self.__n_times_answered_correctly

    def increment_num_times_answered_correctly(self) -> None:
        self.__n_times_answered_correctly = self.__n_times_answered_correctly + 1

    def get_accuracy(self) -> float:
        return self.__n_times_answered_correctly / self.__n_times_asked

    def get_last_date_asked(self) -> time:
        return self.__last_date_asked

    def update_last_date_asked(self) -> None:
        self.__last_date_asked = time.time()

    def get_related_skills(self) -> List[Skills]:
        return self.__related_skills

    def set_related_skills(self, skills: List[Skills]) -> None:
        self.__related_skills = skills

    def get_tags(self) -> List[str]:
        return self.__tags

    def set_tags(self, tags: List[str]) -> None:
        self.__tags = tags
