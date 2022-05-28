import enum

class Skills(enum.Enum):
    # STR (100)
    # STA (200)
    # DEX (300)
    MUSIC_TECHNIQUE = 300
    FIGHT_TECHNIQUE = 301
    # CON (400)
    # INT (500)
    STEM = 500
    HUMANITIES = 501
    ARTS = 502
    FIGHT_CONCEPTS = 504
    LINGUISTICS = 505
    SURVIVAL_CONCEPTS = 506
    # WIS (600)
    ACUMEN = 600
    AWARENESS = 601
    INSIGHT = 602
    SURVIVAL_APPLICATIONS = 603
    # CHA (700)
    MUSIC_PERFORMANCE = 700
    FIGHT_PERFORMANCE = 701
    PERSUASION = 702
    PEOPLE_READING = 703
    # WIL (800)


skillsMap = {
    Skills.MUSIC_TECHNIQUE.value: "Music-Technique",
    Skills.FIGHT_TECHNIQUE.value: "Fight-Technique",
    Skills.STEM.value: "STEM",
    Skills.HUMANITIES.value: "Humanities",
    Skills.ARTS.value: "Arts",
    Skills.FIGHT_CONCEPTS.value: "Fight-Concepts",
    Skills.LINGUISTICS.value: "Linguistics",
    Skills.SURVIVAL_CONCEPTS.value: "Survival-Concepts",
    Skills.ACUMEN.value: "Acumen",
    Skills.AWARENESS.value: "Awareness",
    Skills.INSIGHT.value: "Insight",
    Skills.SURVIVAL_APPLICATIONS.value: "Survival-Applications",
    Skills.MUSIC_PERFORMANCE.value: "Music-Performance",
    Skills.FIGHT_PERFORMANCE.value: "Fight-Performance",
    Skills.PERSUASION.value: "Persuasion",
    Skills.PEOPLE_READING.value: "People Reading"
}
