import time

from .IQuest import IQuest
from ..enums.CoreStats import CoreStats
from ..enums.Skills import Skills
from ..enums.QuestDuration import QuestDuration
from ..enums.QuestStatus import QuestStatus
from typing import List

class Quest(IQuest):

    def __init__(self, idNum: int, title: str, description: str, stats: List[CoreStats], skills: List[Skills], duration: QuestDuration, conditions_for_success: List[str], status: QuestStatus, tags: List[str], notes: List[str], startTime: time = time.time()):
        self.__id = idNum
        self.__title = title
        self.__description = description
        self.__stats = stats
        self.__skills = skills
        self.__duration = duration
        self.__conditions_for_success = conditions_for_success
        self.__status = status
        self.__tags = tags
        self.__notes = notes
        self.__start_time = startTime

    @classmethod
    def from_dict(cls, attrDict) -> IQuest:
        return cls(attrDict["id"], attrDict["title"], attrDict["description"], attrDict["stats"], attrDict["skills"], attrDict["duration"], attrDict["conditions_for_success"], attrDict["status"], attrDict["tags"], attrDict["notes"], attrDict["start_time"])

    def get_id(self) -> int:
        return self.__id

    def get_title(self) -> str:
        return self.__title

    def get_description(self) -> str:
        return self.__description

    def get_stats(self) -> List[CoreStats]:
        return self.__stats

    def get_skills(self) -> List[Skills]:
        return self.__skills

    def get_duration(self) -> QuestDuration:
        """In days"""
        return self.__duration

    def get_start_time(self) -> time:
        return self.__start_time

    def get_conditions_for_success(self) -> List[str]:
        return self.__conditions_for_success

    def set_conditions_for_success(self, conditions_for_success: List[str]) -> None:
        self.__conditions_for_success = conditions_for_success

    def get_status(self) -> QuestStatus:
        return self.__status

    def set_status(self, status: QuestStatus) -> None:
        self.__status = status

    def get_tags(self) -> List[str]:
        return self.__tags

    def set_tags(self, tags: List[str]) -> None:
        self.__tags = tags

    def get_notes(self) -> List[str]:
        return self.__notes

    def set_notes(self, notes: List[str]) -> None:
        self.__notes = notes
