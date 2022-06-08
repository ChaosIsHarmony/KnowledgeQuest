import enum

class Skills(enum.Enum):
    # STR (100)
    ATHLETICS = 100
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
    ECONOMICS = 507
    # WIS (600)
    ACUMEN = 600
    AWARENESS = 601
    INSIGHT = 602
    SURVIVAL_APPLICATIONS = 603
    FIGHT_APPLICATIONS = 604
    # CHA (700)
    PERFORMANCE = 700
    PERSUASION = 701
    PEOPLE_READING = 702
    # WIL (800)


skillsMap = {
    Skills.ATHLETICS.value: "Atheltics",
    Skills.MUSIC_TECHNIQUE.value: "Music-Technique",
    Skills.FIGHT_TECHNIQUE.value: "Fight-Technique",
    Skills.STEM.value: "STEM",
    Skills.HUMANITIES.value: "Humanities",
    Skills.ARTS.value: "Arts",
    Skills.FIGHT_CONCEPTS.value: "Fight-Concepts",
    Skills.LINGUISTICS.value: "Linguistics",
    Skills.SURVIVAL_CONCEPTS.value: "Survival-Concepts",
    Skills.ECONOMICS.value: "Economics",
    Skills.ACUMEN.value: "Acumen",
    Skills.AWARENESS.value: "Awareness",
    Skills.INSIGHT.value: "Insight",
    Skills.FIGHT_APPLICATIONS.value: "Fight-Applications",
    Skills.SURVIVAL_APPLICATIONS.value: "Survival-Applications",
    Skills.PERFORMANCE.value: "Performance",
    Skills.PERSUASION.value: "Persuasion",
    Skills.PEOPLE_READING.value: "People Reading"
}
