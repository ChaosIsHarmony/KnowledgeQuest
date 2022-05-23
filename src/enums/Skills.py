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
    Skills.POWER: "Physical-Power",
    Skills.STAMINA: "Physical-Stamina",
    Skills.MUSIC_TECHNIQUE: "Music-Technique",
    Skills.FIGHT_TECHNIQUE: "Fight-Technique",
    Skills.STEM: "STEM",
    Skills.HUMANITIES: "Humanities",
    Skills.ARTS: "Arts",
    Skills.FIGHT_CONCEPTS: "Fight-Concepts",
    Skills.LINGUISTICS: "Linguistics",
    Skills.ACUMEN: "Acumen",
    Skills.AWARENESS: "Awareness",
    Skills.INSIGHT: "Insight",
    Skills.SURVIVAL: "Survival",
    Skills.MUSIC_PERFORMANCE: "Music-Performance",
    Skills.FIGHT_PERFORMANCE: "Fight-Performance",
    Skills.PERSUASION: "Persuasion"
}
