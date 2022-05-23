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
    CoreStats.STRENGTH.value: "STR",
    CoreStats.DEXTERITY.value: "DEX",
    CoreStats.CONSTITUTION.value: "CON",
    CoreStats.WISDOM.value: "WIS",
    CoreStats.INTELLIGENCE.value: "INT",
    CoreStats.CHARISMA.value: "CHA"
}
