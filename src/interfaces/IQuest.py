import time

from abc import ABC, abstractmethod
from ..enums.CoreStats import CoreStats
from ..enums.Skills import Skills
from ..enums.QuestDuration import QuestDuration
from ..enums.QuestStatus import QuestStatus
from typing import List

class IQuest(ABC):

    @abstractmethod
    def get_id(self) -> int:
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
    def get_duration(self) -> QuestDuration:
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
    def get_xp_value(self) -> int:
        pass

    @abstractmethod
    def set_xp_value(self, xp: int) -> None:
        pass
