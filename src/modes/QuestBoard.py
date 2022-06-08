from datetime import datetime, timedelta
import json
import time

from .. import common
from ..interfaces.IQuest import IQuest
from ..enums.CoreStats import CoreStats, coreStatsMap
from ..enums.Skills import Skills, skillsMap
from ..enums.QuestOptions import QuestOptions as Options
from ..enums.QuestStatus import QuestStatus as Status, statusMap

from typing import Dict, List, Tuple, TypeVar

T = TypeVar("T")
PRIMARY = 3
SECONDARY = 2
TERTIARY = 1


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


def get_target_input(default: T, message: str) -> T:
    value = default
    while value == default:
        value = input(message)
        if type(default) == int:
            value = int(value)

    return value


def determine_xp(duration: int, rank: int) -> int:
    '''
    Rank is from 1-3, three being the highest.
    This corresponds to Tertiary, Secondary, Primary importance.
    '''
    return int((duration / 7) * rank)


def determine_skills(duration: int, xpValues: Dict[int, int]) -> Tuple[List[int], Dict[int, int]]:
    for skill in Skills:
        print(f"{skill.value} = {skillsMap[skill.value]}")

    skills = []

    # Primary
    print("Select Primary Skill")
    skillVal = get_target_input(0, "Skill Affected: ")
    skills.append(skillVal)
    xpValues[skillVal] = determine_xp(duration, PRIMARY)

    # Secondary
    print("Select Secondary Skill (-1 if not applicable)")
    skillVal = get_target_input(0, "Skill Affected: ")
    if skillVal >= 0:
        skills.append(skillVal)
        xpValues[skillVal] = determine_xp(duration, SECONDARY)

    # Tertiary
    print("Select Tertiary Skill (-1 if not applicable)")
    skillVal = get_target_input(0, "Skill Affected: ")
    if skillVal >= 0:
        skills.append(skillVal)
        xpValues[skillVal] = determine_xp(duration, TERTIARY)

    return skills, xpValues


def determine_stats(duration: int, xpValues: Dict[int, int]) -> Tuple[List[int], Dict[int, int]]:
    for stat in CoreStats:
        print(f"{stat.value} = {coreStatsMap[stat.value]}")

    stats = []

    # Primary
    print("Select Primary Stat")
    statVal = get_target_input(-2, "Core Stat Affected: ")
    stats.append(statVal)
    xpValues[statVal] = determine_xp(duration, PRIMARY)

    # Secondary
    print("Select Secondary Stat (-1 if not applicable)")
    statVal = get_target_input(-2, "Core Stat Affected: ")
    if statVal >= 0:
        stats.append(statVal)
        xpValues[statVal] = determine_xp(duration, SECONDARY)

    # Tertiary
    print("Select Tertiary Stat (-1 if not applicable)")
    statVal = get_target_input(-2, "Core Stat Affected: ")
    if statVal >= 0:
        stats.append(statVal)
        xpValues[statVal] = determine_xp(duration, TERTIARY)

    return stats, xpValues


def determine_stats_and_skills(duration: int) -> Tuple[List[int], List[int], Dict[int, int]]:
    xpValues = {}
    stats, xpValues = determine_stats(duration, xpValues)
    skills, xpValues = determine_skills(duration, xpValues)

    return stats, skills, xpValues


def create_new_quest(unformattedQuests: List[IQuest], superquest: int = 0, subquests: List[int] = None) -> None:
    # Determine quest details
    title = get_target_input("", "Title: ")
    description = get_target_input("", "Description: ")
    duration = get_target_input(0, "Duration of Quest: ")

    stats, skills, xpValues = determine_stats_and_skills(duration)

    print(stats, skills, xpValues)

    conditionsForSuccess = []
    tags = []
    notes = []

    # auto-init important yet to be determined variables
    idNum = common.get_highest_id(unformattedQuests)
    startTime = 0
    status = 0

    # Determine if should have subquests (loop & recurse)

    # Save new quest


def execute_option(option: Options, unformattedQuests: List[IQuest]) -> None:
    if option == Options.ADD_NEW_QUEST:
        create_new_quest(unformattedQuests)
        return

    if option == Options.START_NEW_QUEST:
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
        validOptions = [option.name[0] for option in Options]
        if userSelection.upper() not in validOptions:
            print("Invalid selection.")
            continue

        if userSelection.upper() == Options.RETURN_TO_MAIN_MENU.name[0]:
            break

        for option in Options:
            if option.name[0] == userSelection.upper():
                execute_option(option, unformattedQuests)
                break
