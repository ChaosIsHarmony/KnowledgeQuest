import json
import time

from ..enums.Skills import Skills
from ..interfaces.IJsonSerializable import IJsonSerializable
from ..interfaces.IQuestion import IQuestion
from typing import Dict, List, TypeVar

T = TypeVar("T")

class Question(IQuestion, IJsonSerializable):

    def __init__(self, idNum: int, question_text: str, answers: List[str], answer: str, n_times_asked: int, n_times_correctly_answered: int, last_asked: time, skills: List[Skills], tags: List[str]):
        self.id = idNum
        self.question_text = question_text
        self.answers = answers
        self.answer = answer
        self.n_times_asked = n_times_asked
        self.n_times_answered_correctly = n_times_correctly_answered
        self.last_asked = last_asked
        self.skills = skills
        self.tags = tags

    def get_id(self) -> int:
        return self.id

    def get_text(self) -> str:
        return self.question_text

    def get_answers(self) -> List[str]:
        return self.answers

    def get_answer(self) -> str:
        return self.answer

    def get_num_times_asked(self) -> int:
        return self.n_times_asked

    def increment_num_times_asked(self) -> None:
        self.n_times_asked = self.n_times_asked + 1

    def get_num_times_answered_correctly(self) -> int:
        return self.n_times_answered_correctly

    def increment_num_times_answered_correctly(self) -> None:
        self.n_times_answered_correctly = self.n_times_answered_correctly + 1

    def get_accuracy(self) -> float:
        if self.n_times_asked > 0:
            return self.n_times_answered_correctly / self.n_times_asked
        else:
            return 0.0

    def get_last_asked(self) -> time:
        return self.last_asked

    def update_last_asked(self) -> None:
        self.last_asked = time.time()

    def get_related_skills(self) -> List[Skills]:
        return self.related_skills

    def set_related_skills(self, skills: List[Skills]) -> None:
        self.related_skills = skills

    def get_tags(self) -> List[str]:
        return self.tags

    def set_tags(self, tags: List[str]) -> None:
        self.tags = tags

    def to_json(self) -> Dict[str, T]:
        return self.__dict__

    def __str__(self) -> str:
        return f"ID: {self.id} | N_TIMES_ASKED: {self.n_times_asked}"
