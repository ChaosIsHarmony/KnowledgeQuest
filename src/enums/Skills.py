import enum

class Skills(enum.Enum):
    # STR
    POWER = 100
    STAMINA = 101
    # DEX
    MUSIC_TECHNIQUE = 200
    FIGHT_TECHNIQUE = 201
    # INT
    STEM = 300
    HUMANITIES = 301
    ARTS = 302
    FIGHT_CONCEPTS = 304
    LINGUISTICS = 305
    # WIS
    ACUMEN = 400
    AWARENESS = 401
    INSIGHT = 402
    SURVIVAL = 403
    # CHA
    MUSIC_PERFORMANCE = 500
    FIGHT_PERFORMANCE = 501
    PERSUASION = 502


skillsMap = {
    Skills.POWER.value: "Physical-Power",
    Skills.STAMINA.value: "Physical-Stamina",
    Skills.MUSIC_TECHNIQUE.value: "Music-Technique",
    Skills.FIGHT_TECHNIQUE.value: "Fight-Technique",
    Skills.STEM.value: "STEM",
    Skills.HUMANITIES.value: "Humanities",
    Skills.ARTS.value: "Arts",
    Skills.FIGHT_CONCEPTS.value: "Fight-Concepts",
    Skills.LINGUISTICS.value: "Linguistics",
    Skills.ACUMEN.value: "Acumen",
    Skills.AWARENESS.value: "Awareness",
    Skills.INSIGHT.value: "Insight",
    Skills.SURVIVAL.value: "Survival",
    Skills.MUSIC_PERFORMANCE.value: "Music-Performance",
    Skills.FIGHT_PERFORMANCE.value: "Fight-Performance",
    Skills.PERSUASION.value: "Persuasion"
}
