from datetime import datetime, timedelta
import json
import time

from .. import common
from ..interfaces.IQuest import IQuest
from ..enums.CoreStats import CoreStats, coreStatsMap
from ..enums.Skills import Skills, skillsMap
from ..enums.QuestOptions import QuestOptions as Options
from ..enums.QuestStatus import QuestStatus as Status, statusMap

from typing import Dict, List, TypeVar

T = TypeVar("T")


def fetch_quests(path: str) -> List[IQuest]:
    questFileContents = common.load_file(path)
    quests = common.deserialize_quests(questFileContents)

    return quests


def get_end_date(start: time, duration: int) -> str:
    """YYYY-MM-DD"""
    date = datetime.fromtimestamp(start)
    endDate = date + timedelta(days=duration)
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


def format_quests(ongoingQuests: List[IQuest]) -> List[str]:
    formattedQuests = []
    for quest in ongoingQuests:
        questStr = "***************\n"
        questStr += f"QUEST-ID: {quest.get_id()}\n"
        questStr += f"TITLE: {quest.get_title()}\n"
        questStr += f"STATS AFFECTED: {create_str_from_list(quest.get_stats(), coreStatsMap)}\n"
        questStr += f"SKILLS AFFECTED: {create_str_from_list(quest.get_skills(), skillsMap)}\n"
        questStr += f"ENDS ON: {get_end_date(quest.get_start_time(), quest.get_duration())}\n"
        questStr += "***************\n"

        formattedQuests.append(questStr)


    return formattedQuests


def quest_requires_update(quest: IQuest) -> bool:
    print(quest.get_status())
    # status is not on-going
    if quest.get_status() != Status.ON_GOING:
        return False

    # get dates for comparison (quest's end date and today's date)
    date = datetime.fromtimestamp(quest.get_start_time())
    endDate = date + timedelta(days=quest.get_duration())
    currentDate = datetime.now()

    return endDate < currentDate


def display_quests_requiring_status_update(unformattedQuests: List[IQuest]) -> None:
    questsToUpdate = list(filter(lambda q: quest_requires_update(q), unformattedQuests))
    otherQuests = list(filter(lambda q: not quest_requires_update(q), unformattedQuests))

    for quest in questsToUpdate:
        formattedQuest = format_quests([quest])[0]
        print(formattedQuest)
        status = -1
        while status != Status.SUCCESS.value and status != Status.FAILURE.value:
            status = int(input("Success (2) or Failure (3)? "))

        quest.set_status(statusMap[status])
        print("Status updated!")

    # recombine all quests and update file
    if len(questsToUpdate) > 0:
        otherQuests.extend(questsToUpdate)
        common.write_file(otherQuests, common.QUESTS_FILEPATH)

    print("All quests are up-to-date.")


def display_ongoing_quests(unformattedQuests: List[IQuest]) -> None:
    ongoingQuests = list(filter(lambda q: q.get_status() == Status.ON_GOING, unformattedQuests))
    formattedQuests = format_quests(ongoingQuests)

    for quest in formattedQuests:
        print(quest)


def create_new_quest(unformattedQuests: List[IQuest], superquest: int = 0, subquests: List[int] = None) -> None:
    # Determine quest details
    title = ""
    description = ""
    stats = []
    skills = []
    xpValues = {}
    duration = 0
    conditionsForSuccess = []
    tags = []
    notes = []

    # auto-init important yet to be determined variables
    idNum = common.get_highest_question_id(unformattedQuests)
    startTime = 0
    status = 0

    # Determine if should have subquests (loop & recurse)

    # Save new quest

    pass


def execute_option(option: Options, unformattedQuests: List[IQuest]) -> None:
    if option == Options.ADD_NEW_QUEST.name[0]:
        create_new_quest(unformattedQuests)
        return

    if option == Options.START_NEW_QUEST.name[0]:
        start_new_quest()
        return


def run() -> None:
    unformattedQuests = fetch_quests(common.QUESTS_FILEPATH)

    # Check if a quest has recently reached its time limit
    display_quests_requiring_status_update(unformattedQuests)

    # Display ON-GOING quests & their statuses
    #   A Long Quest is composed of multiple Medium Quests
    #   A Medium Quest is composed of multiple Short Quests
    #   Short Quests = approx. 1 week
    #   Medium Quests = approx. 1 month
    #   Long Quests are multi-month
    display_ongoing_quests(unformattedQuests)

    # Query user's desired action
    while (True):
        print("Here are your options [type first letter of selection]:")
        for option in Options:
            print(option.name)

        userSelection = input("")
        if userSelection.upper() not in [option.name for option in Options]:
            print("Invalid selection.")
            continue

        if userSelection.upper() == Options.RETURN_TO_MAIN_MENU.name[0]:
            break

        for option in Options:
            if option.name == userSelection.upper():
                execute_option(option, unformattedQuests)
