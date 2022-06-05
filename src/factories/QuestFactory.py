from ..interfaces.IQuest import IQuest
from ..entities.Quest import Quest

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
                     attrDict["status"],
                     attrDict["tags"],
                     attrDict["notes"],
                     attrDict["start_time"],
                     attrDict["xp_values"])


