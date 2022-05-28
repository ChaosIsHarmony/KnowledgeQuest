import time

from ..enums.Skills import Skills
from abc import ABC, abstractmethod
from typing import List

class IQuestion(ABC):

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_question_text(self) -> str:
        pass

    @abstractmethod
    def get_question_answers(self) -> List[str]:
        pass

    @abstractmethod
    def get_answer(self) -> str:
        pass

    @abstractmethod
    def get_num_times_asked(self) -> int:
        pass

    @abstractmethod
    def increment_num_times_asked(self) -> None:
        pass

    @abstractmethod
    def get_num_times_answered_correctly(self) -> int:
        pass

    @abstractmethod
    def increment_num_times_answered_correctly(self) -> None:
        pass

    @abstractmethod
    def get_accuracy(self) -> float:
        pass

    @abstractmethod
    def get_last_asked(self) -> time:
        pass

    @abstractmethod
    def update_last_asked(self) -> None:
        pass

    @abstractmethod
    def get_related_skills(self) -> List[Skills]:
        pass

    @abstractmethod
    def set_related_skills(self, skills: List[Skills]) -> None:
        pass

    @abstractmethod
    def get_tags(self) -> List[str]:
        pass

    @abstractmethod
    def set_tags(self, tags: List[str]) -> None:
        pass
