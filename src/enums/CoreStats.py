import enum

class CoreStats(enum.Enum):
    """
    Strength (STR): raw, physical power.

    Dexterity (DEX): agility and finesse.

    Constitution (CON): fortitude and endurance.

    Wisdom (WIS): perception and insight (topic-independent).

    Intelligence (INT): reasoning and memory (topic-specific).

    Charisma (CHA): people-wrangling.
    """
    STRENGTH = 0
    DEXTERITY = 1
    CONSTITUTION = 2
    WISDOM = 3
    INTELLIGENCE = 4
    CHARISMA = 5

coreStatsMap = {
    CoreStats.STRENGTH: "STR",
    CoreStats.DEXTERITY: "DEX",
    CoreStats.CONSTITUTION: "CON",
    CoreStats.WISDOM: "WIS",
    CoreStats.INTELLIGENCE: "INT",
    CoreStats.CHARISMA: "CHA"
}
