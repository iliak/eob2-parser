from enum import Enum

from dice import Dice
from location import Location
from monster import Monster
from scripts.script import Script
from tools.reader import BinaryReader


class Point:
    """

    """
    x = 0
    y = 0

    def decode(self):
        return {"x": self.x, "y": self.y, }

    def __str__(self):
        """

        :return:
        """
        return "[x:{x} y:{y}]".format(x=self.x, y=self.y)


class Rectangle:
    """

    """
    x = 0
    y = 0
    width = 0
    height = 0

    def decode(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height}

    def __str__(self):
        """

        :return:
        """

        return "[x:{x} y:{y} - width:{width} height:{height}]".format(x=self.x, y=self.y, width=self.width, height=self.height)


class WallMapping:
    """
    Wall-Types: Who can pass
    WF_PASSNONE			0x00  Can be passed by no one
    WF_PARTYPASS		0x01  Can be passed by the player, big item
    WF_SMALLPASS		0x02  Can be passed by a small item
    WF_MONSTERPASS		0x04  Can be passed by a monster
    WF_PASSALL			0x07  Can be passed by all
    WF_ISDOOR			0x08  Is a door
    WF_DOOROPEN			0x10  The door is open
    WF_DOORCLOSED		0x20  The door is closed
    WF_DOORKNOB			0x40  The door has a knob
    WF_ONLYDEC			0x80  No wall, only decoration, items visible

    Wall-Types: Kind
    WT_SOLID			0x01  Is a solid wall, draw top
    WT_SELFDRAW			0x02  Is a stair, for example, no bottom
    WT_DOORSTUCK		0x04  The door is stuck
    WT_DOORMOVES		0x08  The door is opening
    WT_DOOROPEN			0x10  The door is open
    WT_DOORCLOSED		0x20  The door is closed
    """

    def __init__(self):
        self.index = 0  # This is the index used by the .maz file
        self.type = 0  # Index to what backdrop wall type that is being used
        self.decorationId = 0  # Index to an optional overlay decoration image in the DecorationData.decorations
        # array in the [[eob.dat |.dat]] files
        self.eventMask = 0  #
        self.flags = 0  #

    @property
    def is_blocking(self):

        return self.flags & 0x00 == 0x00

    @property
    def is_door(self):

        return self.flags & 0x08 == 0x08

    def __str__(self):

        type = ""
        if self.type & 0x01 == 0x01: type += "WT_SOLID, "
        if self.type & 0x02 == 0x02: type += "WT_SELFDRAW, "
        if self.type & 0x04 == 0x04: type += "WT_DOORSTUCK, "
        if self.type & 0x08 == 0x08: type += "WT_DOORMOVES, "
        if self.type & 0x10 == 0x10: type += "WT_DOOROPEN, "
        if self.type & 0x20 == 0x20: type += "WT_DOORCLOSED, "

        flags = ""
        if self.flags & 0x00 == 0x00: flags += "WF_PASSNONE, "
        if self.flags & 0x01 == 0x01: flags += "WF_PARTYPASS, "
        if self.flags & 0x02 == 0x02: flags += "WF_SMALLPASS, "
        if self.flags & 0x04 == 0x04: flags += "WF_MONSTERPASS, "
        if self.flags & 0x07 == 0x07: flags += "WF_PASSALL, "
        if self.flags & 0x08 == 0x08: flags += "WF_ISDOOR, "
        if self.flags & 0x10 == 0x10: flags += "WF_DOOROPEN, "
        if self.flags & 0x20 == 0x20: flags += "WF_DOORCLOSED, "
        if self.flags & 0x40 == 0x40: flags += "WF_DOORKNOB, "
        if self.flags & 0x80 == 0x80: flags += "WF_ONLYDEC, "

        return "Type: {type} - Flags: {flags}".format(type=type, flags=flags)


class DecorationInfo:
    """

    """

    def __init__(self):
        self.files = None
        self.wallMapping = None

    def __str__(self):
        if self.files:
            return "File '{file}'".format(file=self.files)

        else:
            return "mapping '{mapping}'".format(mapping=self.wallMapping)


class DecorationFilename:
    """
    """

    def __init__(self):
        self.gfx = ""
        self.dec = ""

    def __str__(self):
        return 'gfx: {gfx}.cps - dec:{dec}'.format(gfx=self.gfx, dec=self.dec)


class DoorInfo:
    """
    http://eab.abime.net/showpost.php?p=533880&postcount=374
    http://eab.abime.net/showpost.php?p=579468&postcount=405
    """

    def __init__(self):
        self.command = None
        self.idx = None
        self.type = None
        self.knob = None
        self.gfxFile = ""
        self.doorRectangles = [Rectangle() for i in range(3)]  # rectangles in door?.cps size [3]
        self.buttonRectangles = [Rectangle() for i in range(2)]  # rectangles in door?.cps size [2]
        self.buttonPositions = [Point() for i in range(2)]  # x y position where to place door button size [2,2]

    def decode(self):
        return {"command": self.command, "idx": self.idx, "type": self.type, "knob": self.knob, "gfxFile": self.gfxFile, "doorRectangle": [rect.decode() for rect in self.doorRectangles],
                "buttons": {"rectangles": [rect.decode() for rect in self.buttonRectangles], "positions": [point.decode() for point in self.buttonPositions], }}


class MonsterType:
    """

    """

    def __init__(self):
        self.index = 0
        self.unk0 = None
        self.thac0 = 0
        self.unk1 = None
        self.hp_dice = Dice()
        self.number_of_attacks = 0
        self.attack_dice = [Dice() for i in range(3)]
        self.special_attack_flag = 0
        self.abilities_flags = 0
        self.unk2 = None
        self.exp_gain = 0
        self.size = 0
        self.attack_sound = 0
        self.move_sound = 0
        self.unk3 = None
        self.is_attack2 = 0
        self.distant_attack = 0
        self.max_attack_count = 0
        self.attack_list = [None for i in range(5)]
        self.turn_undead_value = 0
        self.unk4 = None
        self.unk5 = [None for i in range(3)]

    def decode(self):
        return {"index":            self.index, "unknown0": self.unk0, "thac0": self.thac0, "unknown1": self.unk1, "hp": self.hp_dice.decode(), "attacks": {"count":           self.number_of_attacks,
                                                                                                                                                            "dices":           [dice.decode()
                                                                                                                                                                                for dice in
                                                                                                                                                                                self.attack_dice],
                                                                                                                                                            "special_flags":   self.special_attack_flag,
                                                                                                                                                            "abilities_flags": self.abilities_flags,
                                                                                                                                                            "sound":           self.attack_sound,
                                                                                                                                                            "distant":         self.distant_attack, },
                "unknown2":         self.unk2, "exp_gain": self.exp_gain, "size": self.size, "move_sound": self.mouve_sound, "unknown3": self.unk3, "is_attack2": self.is_attack2,
                "max_attack_count": self.max_attack_count, "attack_list": [i for i in self.attack_list], "turn_undead": self.turn_undead_value, "unknown4": self.unk4,
                "unknown5":         [i for i in self.unk5], }


class MonsterGfx:
    """

    """

    def __init__(self):
        self.used = False
        self.load_prog = None
        self.unk0 = None
        self.unk1 = None
        self.label = ""

    def decode(self):
        return {"used": self.used, "load_prog": self.load_prog, "unknown0": self.unk0, "unknown1": self.unk1, "label": self.label}

    def __str__(self):
        return self.label


class TriggerFlag(Enum):
    """
    Flags used to trigger events
    """
    OnPartyEnter = 0x08
    OnPartyLeave = 0x10
    OnPutItem = 0x20
    OnGetItem = 0x40
    OnthrowItem = 0x80
    OnClick = 0x800


class Trigger:
    """

    """
    def __init__(self, reader=None):
        """

        :param reader:
        """
        self.location = None
        self.flags = None
        self.offset = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.location = Location(reader)
        self.flags = reader.read_ushort()
        self.offset = reader.read_ushort()

    def run(self, maze, assets):
        """

        :return:
        """
        return {"offset": f"0x{self.offset:04X}", "flags": f"0x{self.flags:02X}"}

    def __str__(self):
        return "{location}: offset: 0x{offset:04X}, flags: 0x{flags:04X}".format(location=self.location, offset=self.offset, flags=self.flags)


class Header:
    """

    """

    def __init__(self):
        self.mazeName = None
        self.vmpVncName = None
        self.paletteName = None
        self.soundName = None
        self.doors = [DoorInfo() for i in range(2)]
        self.monsterGfx = [MonsterGfx() for i in range(2)]
        self.monsterTypes = []  # [MonsterType() for i in range(35)]
        self.decorations = []
        self.max_monsters = None
        self.next_hunk = None

    def decode(self):
        return {"mazeName":     self.mazeName, "vmpVncName": self.vmpVncName, "palette": self.paletteName, "sound": self.soundName, "doors": [door.decode() for door in self.doors],
                "monsters":     {"gfx": [gfx.decode() for gfx in self.monsterGfx], "types": [type.decode() for type in self.monsterTypes], },
                "decorations":  [None for deco in self.decorations],
                "max_monsters": self.max_monsters, 'next_hunk': self.next_hunk, }


class Inf:
    """

    """

    def __init__(self, name):

        self.name = name
        self.timers = []
        self.monsters = []
        self.headers = [Header() for i in range(2)]
        self.hunks = [0, 0]
        self.triggers = []
        self.messages = []
        self.script = None

        self.width = 0
        self.height = 0  # self.walls = []

    def process(self, filename):
        """

        :param filename:
        :return:
        """

        # http://grimwiki.net/wiki/EobConverter
        # LEVEL*.MAZ files are stored in PAK files, so you need to extract PAK to extract them first. MAZ files
        # contain dungeon layout (walls, doors, buttons etc.). It does not contain information about items.
        #
        # First 6 bytes constitute a header:
        #
        #     uint16_t width - specifies dungeon width (EOB1 levels always use 32)
        #     uint16_t height - specifies dungeon height (EOB1 levels always use 32)
        #     uint16_t unknown - EOB1 levels seem to have value 0x0004 here. One interpretation is that it may be a
        #                        number of bytes for each grid.
        #
        # Header is followed by width x height grid definitions. Each grid takes 4 bytes. For all EOB1 MAZ levels,
        # that gives 32x32x4 = 4096 bytes. Together with 6 bytes (header), this results in each file having length
        #  of 4102 bytes.
        #
        # Each grid is described by 4 octets. Each character specifies how a given grid looks from W, S, E and N,
        # respectively. It is possible to define inconsistent grids (e.g. look like doors when looked up front, but
        # look like a pressure plate when seen from sides).
        #
        #     0x00 - empty corridor
        #     0x01 - wall (pattern 1)
        #     0x02 - wall (pattern 2)
        #     0x03 - door without a button (closed) opening
        #     0x04 - door opening 1
        #     0x05 - door opening1
        #     0x07 - door opened
        #     0x08 - door with a button (closed)
        #     0x09 - door opening2
        #     0x0a - door opening2
        #     0x0b - door opening2
        #     0x0c - a ladder leading down
        #     0x0d - door with a button (open)
        #     0x11 - door opened
        #     0x12 - door closed
        #     0x13 - door opening4
        #     0x14 - door opening4
        #     0x15 - door opening4
        #     0x16 - door opened
        #     0x17 - up stair/ladder
        #     0x18 - fake ladder leading down (used in inaccessible part of level 1, probably by EOB developers for testing)
        #     0x19 - blocker
        #     0x1a - hole in the ceiling (from upper level)
        #     0x1b - pressure plate
        #     0x1c - pressure plate
        #     0x1d - normal alcove
        #     0x1f - pressure plate
        #     0x20 - switch
        #     0x23 - dalle(inter)
        #     0x24 - dalle(inter)
        #     0x25 - hole (ceilar)
        #     0x26 - hole (floor)
        #     0x27 - hidden button (large pushable brick)
        #     0x2a - hidden switch
        #     0x2b - drainage at the floor level (decoration)
        #     0x2c - "rat hole" - drainage at the floor level with eyes (decoration) or teleport
        #     0x33 - door to force
        #     0x36 - stone portal
        #     0x37 - lever
        #     0x3c - normal button, small brick sized
        #     0x3e - rat hole
        #     0x3f - sewer pipe (in the middle)
        #     0x41 - rune 'entrance'
        #     0x45 - cave-in or stone portal

        with BinaryReader(filename + '.INF') as reader:

            # hunk 1
            self.hunks[0] = reader.read_ushort()

            # region Headers
            for header in self.headers:

                if reader.offset < self.hunks[0]:
                    header.next_hunk = reader.read_ushort()
                    b = reader.read_ubyte()
                    if b == 0xEC:
                        header.mazeName = reader.read_string(13)
                        header.vmpVncName = reader.read_string(13)

                    b = reader.read_ubyte()
                    if b != 0xFF:
                        header.paletteName = reader.read_string(13)

                    header.soundName = reader.read_string(13)

                    # region Door name & Positions + offset
                    for door in header.doors:

                        b = reader.read_ubyte()
                        if b in (0xEC, 0xEA):
                            door.gfxFile = reader.read_string(13)
                            door.idx = reader.read_ubyte()
                            door.type = reader.read_ubyte()
                            door.knob = reader.read_ubyte()

                            for rect in door.doorRectangles:
                                rect.x = reader.read_ushort()
                                rect.y = reader.read_ushort()
                                rect.width = reader.read_ushort()
                                rect.height = reader.read_ushort()

                            for rect in door.buttonRectangles:
                                rect.x = reader.read_ushort()
                                rect.y = reader.read_ushort()
                                rect.width = reader.read_ushort()
                                rect.height = reader.read_ushort()

                            for pt in door.buttonPositions:
                                pt.x = reader.read_ushort()
                                pt.y = reader.read_ushort()
                    # endregion

                    # region Monsters graphics informations
                    header.max_monsters = reader.read_ushort()
                    for i in range(2):
                        b = reader.read_ubyte()
                        if b == 0xEC:
                            gfx = MonsterGfx()
                            gfx.load_prog = reader.read_ubyte()
                            gfx.unk0 = reader.read_ubyte()
                            gfx.label = reader.read_string(13)
                            gfx.unk1 = reader.read_ubyte()

                            header.monsterGfx[i] = gfx
                    # endregion

                    # region Monster definitions
                    while True:
                        b = reader.read_ubyte()
                        if b == 0xFF:
                            break

                        type = MonsterType()
                        type.index = b
                        type.unk0 = reader.read_ubyte()
                        type.thac0 = reader.read_ubyte()
                        type.unk1 = reader.read_ubyte()

                        type.hp_dice.process(reader)

                        type.number_of_attacks = reader.read_ubyte()
                        for dice in type.attack_dice:
                            dice.process(reader)

                        type.special_attack_flag = reader.read_ushort()
                        type.abilities_flags = reader.read_ushort()
                        type.unk2 = reader.read_ushort()
                        type.exp_gain = reader.read_ushort()
                        type.size = reader.read_ubyte()
                        type.attack_sound = reader.read_ubyte()
                        type.move_sound = reader.read_ubyte()
                        type.unk3 = reader.read_ubyte()

                        b = reader.read_ubyte()
                        if b != 0xFF:
                            type.is_attack2 = True
                            type.distant_attack = reader.read_ubyte()
                            type.max_attack_count = reader.read_ubyte()
                            for i in range(type.max_attack_count):
                                type.attack_list[i] = reader.read_ubyte()
                                reader.read_ubyte()

                        type.turn_undead_value = reader.read_byte()
                        type.unk4 = reader.read_ubyte()
                        type.unk5 = reader.read_ubyte(3)

                        header.monsterTypes.append(type)

                    # endregion

                    # region Wall decorations
                    b = reader.read_ubyte()
                    if b != 0xFF:
                        decorateblocks = reader.read_ushort()
                        for i in range(decorateblocks):
                            b = reader.read_ubyte()
                            deco = DecorationInfo()
                            if b == 0xEC:
                                deco.files = DecorationFilename()
                                deco.files.gfx = reader.read_string(13)
                                deco.files.dec = reader.read_string(13)
                            elif b == 0xFB:
                                deco.wallMapping = WallMapping()
                                deco.wallMapping.shapeId = reader.read_byte()
                                deco.wallMapping.type = reader.read_ubyte()
                                deco.wallMapping.decorationId = reader.read_byte()
                                deco.wallMapping.eventMask = reader.read_ubyte()
                                deco.wallMapping.flags = reader.read_ubyte()
                            else:
                                pass

                            header.decorations.append(deco)
                    # endregion

                    # Padding
                    while reader.read_uint() != 0xFFFFFFFF:
                        pass
            # endregion

            self.hunks[1] = reader.read_ushort()

            # region Monsters
            b = reader.read_ubyte()
            if b != 0xFF:
                # Timers
                while reader.read_ubyte() != 0xFF:
                    self.timers.append(reader.read_ubyte())

                # Descriptions
                for i in range(30):
                    monster = Monster()
                    monster.index = reader.read_byte()
                    monster.timer_id = reader.read_ubyte()
                    monster.location = Location(reader)
                    monster.sub_position = reader.read_ubyte()
                    monster.direction = reader.read_ubyte()
                    monster.type = reader.read_ubyte()
                    monster.picture_index = reader.read_ubyte()
                    monster.phase = reader.read_ubyte()
                    monster.pause = reader.read_ubyte()
                    monster.weapon = reader.read_ushort()
                    monster.pocket_item = reader.read_ushort()

                    self.monsters.append(monster)

            # endregion

            # Scripts
            self.script = Script(reader)

            # region Messages
            while reader.offset < self.hunks[1]:
                self.messages.append(reader.search_string())

            # endregion

            # region Triggers
            trigger_count = reader.read_ushort()
            for i in range(trigger_count):
                trigger = Trigger(reader)
                self.triggers.append(trigger)

            # endregion

    def decode(self, assets):
        return {
            "name":     self.name,
            "width":    self.width,
            "height":   self.height,
            "timers":   [timer for timer in self.timers],
            # "headers": [header.decode() for header in self.headers],
            # "hunks": [hunk for hunk in self.hunks],
            "triggers": {trigger.location.coordinates(): trigger.run(self, assets) for trigger in self.triggers},
            "messages": {k: v for k, v in enumerate(self.messages)},
            "scripts":  self.script.run(self, assets),
            "monsters": [],
        }


def inf_decode():
    """

    :return:
    """
    files = [
        'LEVEL1',
        'LEVEL2',
        'LEVEL3',
        'LEVEL4',
        'LEVEL5',
        'LEVEL6',
        'LEVEL7',
        'LEVEL8',
        'LEVEL9',
        'LEVEL10',
        'LEVEL11',
        'LEVEL12',
        'LEVEL13',
        'LEVEL14',
        'LEVEL15',
        'LEVEL16',
    ]
    infs = {}

    for file in files:
        inf = Inf(file)
        inf.process(f'data/{file}')
        infs[file] = inf

    return infs
