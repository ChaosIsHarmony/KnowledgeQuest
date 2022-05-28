import enum

class CoreStats(enum.Enum):
    """
    PHYSICAL STATS
    --------------
    Strength (STR): raw, physical power.
    Stamina (STA): endurance during physical exertion.
    Dexterity (DEX): agility and finesse.
    Constitution (CON): physical resistance.

    MENTAL STATS
    ------------
    Wisdom (WIS): perception and insight (topic-independent).
    Intelligence (INT): reasoning and memory (topic-specific).
    Charisma (CHA): people-wrangling.
    Willpower (WIL): mental resistance.
    """
    # PHYSICAL
    STRENGTH = 0
    STAMINA = 1
    DEXTERITY = 2
    CONSTITUTION = 3
    # MENTAL
    WISDOM = 4
    INTELLIGENCE = 5
    CHARISMA = 6
    WILLPOWER = 7

coreStatsMap = {
    CoreStats.STRENGTH.value: "STR",
    CoreStats.STAMINA.value: "STA",
    CoreStats.DEXTERITY.value: "DEX",
    CoreStats.CONSTITUTION.value: "CON",
    CoreStats.WISDOM.value: "WIS",
    CoreStats.INTELLIGENCE.value: "INT",
    CoreStats.CHARISMA.value: "CHA",
    CoreStats.WILLPOWER.value: "WIL"
}
