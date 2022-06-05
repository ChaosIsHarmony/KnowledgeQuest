import time

from ..interfaces.IJsonSerializable import IJsonSerializable
from ..interfaces.IQuest import IQuest
from ..enums.CoreStats import CoreStats
from ..enums.Skills import Skills
from ..enums.QuestStatus import QuestStatus
from typing import Dict, List, TypeVar

T = TypeVar("T")

class Quest(IQuest, IJsonSerializable):

    def __init__(self, idNum: int, subquests: List[int], superquests: List[int], title: str, description: str, stats: List[CoreStats], skills: List[Skills], duration: int, conditions_for_success: List[str], status: QuestStatus, tags: List[str], notes: List[str], xp_values: Dict[str, int], startTime: time):
        self.id = idNum
        self.subquests = subquests
        self.superquests = superquests
        self.title = title
        self.description = description
        self.stats = stats
        self.skills = skills
        self.duration = duration
        self.conditions_for_success = conditions_for_success
        self.status = status
        self.tags = tags
        self.notes = notes
        self.xp_values = xp_values
        self.start_time = startTime

    def get_id(self) -> int:
        return self.id

    def get_subquests(self) -> List[int]:
        return self.subquests

    def get_superquests(self) -> List[int]:
        return self.superquests

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_stats(self) -> List[CoreStats]:
        return self.stats

    def get_skills(self) -> List[Skills]:
        return self.skills

    def get_duration(self) -> int:
        """In days"""
        return self.duration

    def get_start_time(self) -> time:
        return self.start_time

    def get_conditions_for_success(self) -> List[str]:
        return self.conditions_for_success

    def set_conditions_for_success(self, conditions_for_success: List[str]) -> None:
        self.conditions_for_success = conditions_for_success

    def get_status(self) -> QuestStatus:
        return self.status

    def set_status(self, status: QuestStatus) -> None:
        self.status = status

    def get_tags(self) -> List[str]:
        return self.tags

    def set_tags(self, tags: List[str]) -> None:
        self.tags = tags

    def get_notes(self) -> List[str]:
        return self.notes

    def set_notes(self, notes: List[str]) -> None:
        self.notes = notes

    def get_xp_values(self) -> Dict[str, int]:
        return self.xp_values

    def set_xp_values(self, xp: Dict[str, int]) -> None:
        self.xp_values = xp

    def to_json(self) -> Dict[str, T]:
        self.status = self.status.value # must set to int for serialization
        return self.__dict__
