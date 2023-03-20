from commons import directions
from location import Location


class Monster:
    """
    flags:
    0 = default
    1 = ?
    2 = ?
    3 = ?
    4 = ?
    5 = ?
    6 = ?
    7 = ?
    8 = fear ?
    9 = ?
    10 = ?

        01h-> Active (fighting) has attacked MO_ACT
        02h-> is hit                        MO_HIT
        04h-> Flipflag                      MO_FLIP
        08h-> UNDEAD "Turned"               MO_TURNED
        10h-> set if "turned undead"        MO_FLEE
        20h-> turned to stone               MO_STONE
        40h-> Inactive (at start)           MO_INACT


    Phases:
         -1: raise weapon
         -2: Hit!
          0: Move forward
          1: Move Backwards
          2: Move Left
          3: Move Right
          4: Adjust-Turn
          5: Turn Left
          6: Turn Right
          7: AdjNextHit
          8: Inactive
          9: Walk
         10: Is Hit

    """

    def __init__(self, reader=None):
        """

        """
        self.index = None
        self.timer_id = None
        self.location = None
        self.sub_position = None
        self.direction = None
        self.type = None
        self.picture_index = None
        self.phase = None
        self.pause = None
        self.weapon = None
        self.pocket_item = None

        self.decode(reader)

    def decode(self, reader):
        if not reader:
            return

        self.index = reader.read_ubyte()
        self.timer_id = reader.read_ubyte()
        self.location = Location(reader)
        self.sub_position = reader.read_ubyte()
        self.direction = reader.read_ubyte()
        self.type = reader.read_ubyte()
        self.picture_index = reader.read_ubyte()
        self.phase = reader.read_ubyte()
        self.pause = reader.read_ubyte()
        self.pocket_item = reader.read_ushort()
        self.weapon = reader.read_ushort()

    def __str__(self):
        """

        :return:
        """

        return "ID {index} @ {location}|{subposition} [direction: {direction}, Timer:{timer}, type:{type}, " \
               "picture:{picture}, phase:{phase}, pause:{pause}, weapon:{weapon}, pocket:{pocket}]".format(
            index=self.index, location=self.location, subposition=self.sub_position, direction=directions[self.direction],
            timer=self.timer_id, type=self.type, picture=self.picture_index, phase=self.phase, pause=self.pause,
            weapon=self.weapon, pocket=self.pocket_item
        )
