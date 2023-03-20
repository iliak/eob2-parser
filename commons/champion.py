from enum import Enum, IntFlag


class Class(Enum):
    Fighter = 0x0,
    Ranger = 0x1,
    Paladin = 0x2,
    Mage = 0x3,
    Cleric = 0x4,
    Thief = 0x5,
    FighterCleric = 0x6,
    FighterThief = 0x7,
    FighterMage = 0x8,
    FighterMageThief = 0x9,
    ThiefMage = 0xa,
    ClericThief = 0xb,
    FighterClericMage = 0xc,
    RangerCleric = 0xd,
    ClericMage = 0xe,


class Race(Enum):
    HumanMale = 0x0,
    HumanFemale = 0x1,
    ElfMale = 0x2,
    ElfFemale = 0x3,
    HalfElfMale = 0x4,
    HalfElfFemale = 0x5,
    DwarfMale = 0x6,
    DwarfFemale = 0x7,
    GnomeMale = 0x8,
    GnomeFemale = 0x9,
    HalflingMale = 0xa,
    HalflingFemale = 0xb,


class Alignment(Enum):
    LawfullGood = 0,
    NeutralGood = 1,
    ChaoticGood = 2,
    LawfullNeutral = 3,
    TrueNeutral = 4,
    ChaoticNeutral = 5,
    LawfullEvil = 6,
    NeutralEvil = 7,
    ChaoticEvil = 8,


class HandFlags(IntFlag):
    """

    """
    Primary = 0x0,
    Secondary = 0x1,
    Both = 0x2,


class Champion():
    name = None

    def __str__(self):
        return "{name} ({classe})".format(name=self.name, classe=self.class_)
