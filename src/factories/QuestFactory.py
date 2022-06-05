from ..interfaces.IQuest import IQuest
from ..entities.Quest import Quest
from ..enums.QuestStatus import statusMap

class QuestFactory:

    @classmethod
    def from_dict(cls, attrDict) -> IQuest:
        return Quest(attrDict["id"],
                     attrDict["subquests"],
                     attrDict["superquests"],
                     attrDict["title"],
                     attrDict["description"],
                     attrDict["stats"],
                     attrDict["skills"],
                     attrDict["duration"],
                     attrDict["conditions_for_success"],
                     statusMap[attrDict["status"]], # convert int to QuestStatus
                     attrDict["tags"],
                     attrDict["notes"],
                     attrDict["xp_values"],
                     attrDict["start_time"])


