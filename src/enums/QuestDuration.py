import enum

class QuestDuration(enum.Enum):
    LONG = 0    # Multi-month, 2+ MEDIUM quests
    MEDIUM = 1  # Multi-week, 2+ SHORT quests
    SHORT = 2   # Multi-day, 7-day quest
