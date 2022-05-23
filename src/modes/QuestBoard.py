import datetime
import enum
import json
import time

from ..entities.Quest import Quest
from ..enums.CoreStats import CoreStats, coreStatsMap
from ..enums.Skills import Skills, skillsMap
from ..enums.QuestOptions import QuestOptions as Options
from ..enums.QuestStatus import QuestStatus as Status

from typing import Dict, List, TypeVar


T = TypeVar("T")
QUESTS_FILEPATH = "./data/quests.json"



def load_quests(path: str) -> List[str]:
    contents = []

    try:
        with open(path) as f:
            contents = json.load(f)
    except:
        print("There was a problem loading the quest.json file.")

    return contents


def deserialize_quests(questsJson: List[str]) -> List[Quest]:
    quests = []

    for quest in questsJson:
        quests.append(Quest.from_dict(quest))

    return quests


def fetch_quests(path: str) -> List[Quest]:
    contents = load_quests(path)
    quests = deserialize_quests(contents)

    return quests


def get_end_date(start: time, duration: int) -> str:
    """YYYY-MM-DD"""
    date = datetime.datetime.fromtimestamp(start)
    endDate = date + datetime.timedelta(days=duration)
    return f"{endDate.year}-{endDate.month}-{endDate.day}"


def create_str_from_list(listToUse: List[T], mapToUse: Dict[T, str]) -> str:
    strFromList = ""
    itemsAdded = 0

    for item in listToUse:
        strFromList += mapToUse[item]
        itemsAdded += 1
        if itemsAdded != len(listToUse):
            strFromList += ", "

    return strFromList


def format_quests(ongoingQuests: List[Quest]) -> List[str]:
    formattedQuests = []
    for quest in ongoingQuests:
        questStr = "***************\n"
        questStr += f"TITLE: {quest.get_title()}\n"
        questStr += f"STATS AFFECTED: {create_str_from_list(quest.get_stats(), coreStatsMap)}"
        questStr += f"SKILLS AFFECTED: {create_str_from_list(quest.get_skills(), skillsMap)}"
        questStr += f"ENDS ON: {get_end_date(quest.get_start_time(), quest.get_duration())}\n"

        questStr += "***************\n"

        formattedQuests.append(questStr)


    return formattedQuests



def display_ongoing_quests(unformattedQuests: List[Quest]) -> None:
    ongoingQuests = list(filter(lambda x: x.get_status() == Status.ON_GOING.value, unformattedQuests))
    formattedQuests = format_quests(ongoingQuests)

    for quest in formattedQuests:
        print(quest)


def execute_option(option: Options) -> None:
    pass


def run() -> None:
    unformattedQuests = fetch_quests(QUESTS_FILEPATH)

    # Display ON-GOING quests & their statuses
    #   A Long Quest is composed of multiple Medium Quests
    #   A Medium Quest is composed of multiple Short Quests
    #   Short Quests = approx. 1 week
    #   Medium Quests = approx. 1 month
    #   Long Quests are multi-month
    display_ongoing_quests(unformattedQuests)

    # Query user's desired action
    while (True):
        print("Here are your options:")
        for option in Options:
            print(option.name)

        userSelection = input("")
        if userSelection.upper() not in [option.name for option in Options]:
            print("Invalid selection.")
            continue

        if userSelection.upper() == Options.QUIT.name:
            break

        for option in Options:
            if option.name == userSelection.upper():
                execute_option(option)

