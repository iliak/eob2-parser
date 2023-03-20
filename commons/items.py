from enum import IntFlag


class ItemFlags(IntFlag):
    """
    Item's flags
    """
    Nothing = 0x00,
    Flag01 = 0x01
    ArmorBonus = 0x02
    Flag04 = 0x04  # Enchanted ??
    isVampiric = 0x08  # Sucks damage points from target to attacker
    SpeedBonus = 0x10
    isCursed = 0x20
    isIdentified = 0x40
    GlowMagic = 0x80


class ItemSlotFlags(IntFlag):
    """

    """
    Quiver = 0x01,
    Armour = 0x02,
    Bracers = 0x04,
    Backpack = 0x08,
    Boots = 0x10,
    Helmet = 0x20,
    Necklace = 0x40,
    Belt = 0x80,
    Ring = 0x100,


ItemAction = {
    '0':   'Nothing',
    '1':   '1',
    '2':   'Ammunition',
    '3':   'Use ammunition',
    '4':   'Amulet | coin | eye of talon...',
    '5':   'Open mage spell window',
    '6':   'Open cleric spell window',
    '7':   "Food",
    '8':   "Bones",
    '9':   "Glass sphere | Magic dust | Scroll",
    '10':  "Scroll",
    '11':  "Parchment (something to read)",
    '12':  "Stone item (Cross, Dagger, Gem...)",
    '13':  "Key",
    '14':  "Potion",
    '15':  "Gem",
    '18':  "0x12",
    '19':  "Blow horn (N/S/W/E wind...)",
    '20':  "Amulet of Life or Death",
    '128': "Range Party member",
    '129': "Range Close",
    '130': "Range Medium",
    '131': "Range Long",
    '132': "Lock picks",
    '138': "Amulet",
    '144': "Crimson ring",
    '146': "Wand",
}
