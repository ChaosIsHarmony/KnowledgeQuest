import time

from abc import ABC, abstractmethod
from ..enums.CoreStats import CoreStats
from ..enums.Skills import Skills
from ..enums.QuestStatus import QuestStatus
from typing import Dict, List, TypeVar

T = TypeVar("T")

class IQuest(ABC):

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_subquests(self) -> List[int]:
        pass

    @abstractmethod
    def get_superquests(self) -> List[int]:
        pass

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_stats(self) -> List[CoreStats]:
        pass

    @abstractmethod
    def get_skills(self) -> List[Skills]:
        pass

    @abstractmethod
    def get_duration(self) -> int:
        """In days"""
        pass

    @abstractmethod
    def get_start_time(self) -> time:
        pass

    @abstractmethod
    def get_conditions_for_success(self) -> List[str]:
        pass

    @abstractmethod
    def get_status(self) -> QuestStatus:
        pass

    @abstractmethod
    def get_tags(self) -> List[str]:
        pass

    @abstractmethod
    def get_notes(self) -> List[str]:
        pass

    @abstractmethod
    def get_xp_values(self) -> Dict[str,int]:
        pass

    @abstractmethod
    def set_xp_values(self, xp: Dict[str,int]) -> None:
        pass
