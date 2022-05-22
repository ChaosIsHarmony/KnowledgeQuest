import enum

from .enums.KnowledgeQuestModes import KnowledgeQuestModes as Modes
from .modes import QuestGiver
from .modes import Inquisitor
from .modes import StatsKeeper

def determine_mode() -> Modes:
    """From among listed modes, user selects their preference."""
    print("Choose a mode:")
    for mode in Modes:
        print(mode.name)

    userSelection = input("")

    modeSelected = False
    for mode in Modes:
        if mode.name == userSelection.upper():
            modeSelected = True
            break

    if modeSelected:
        return mode
    else:
        print("Mode not recognized.")
        determine_mode()


def execute_mode(mode: Modes) -> None:
    """Run Selected Mode. Return to Main Menu after."""
    if mode == Modes.QUEST:
        QuestGiver.run()
    elif mode == Modes.QUIZ:
        Inquisitor.run()
    else:
        print(mode)
        StatsKeeper.run()

    backToMain = input("Back to the main menu? [y/n]: ")

    if backToMain == 'y':
        execute_mode(determine_mode())



if __name__ == "__main__":
    execute_mode(determine_mode())
