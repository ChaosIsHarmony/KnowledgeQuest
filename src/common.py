import json

from typing import List

QUESTS_FILEPATH = "./data/quests.json"
QUESTIONS_FILEPATH = "./data/questions.json"


def load_file(path: str) -> List[str]:
    contents = []

    try:
        with open(path) as f:
            contents = json.load(f)
    except:
        print(f"There was a problem loading the file: {path}")

    return contents


