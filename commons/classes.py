from enum import IntFlag

classes = {
    0x00: "Fighter",
    0x01: "Ranger",
    0x02: "Paladin",
    0x03: "Mage",
    0x04: "Cleric",
    0x05: "Thief",
    0x06: "Fighter/Cleric",
    0x07: "Fighter/Thief",
    0x08: "Fighter/Mage",
    0x09: "Fighter/Mage/Thief",
    0x0A: "Thief/Mage",
    0x0B: "Cleric/Thief",
    0x0C: "Fighter/Cleric/Mage",
    0x0D: "Ranger/Cleric",
    0x0E: "Cleric/Mage",
    0x0F: '0x0F',
    0x10: '0x10'
}


class ClassUage(IntFlag):
    """

    """
    Null = 0x00
    Fighter = 0x01
    Mage = 0x02
    Cleric = 0x04
    Thief = 0x08

