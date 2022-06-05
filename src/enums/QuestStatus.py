import enum

class QuestStatus(enum.Enum):
    WAITING = 0
    ON_GOING = 1
    SUCCESS = 2
    FAILURE = 3


statusMap = {
    QuestStatus.WAITING.value: QuestStatus.WAITING,
    QuestStatus.ON_GOING.value: QuestStatus.ON_GOING,
    QuestStatus.SUCCESS.value: QuestStatus.SUCCESS,
    QuestStatus.FAILURE.value: QuestStatus.FAILURE
}
