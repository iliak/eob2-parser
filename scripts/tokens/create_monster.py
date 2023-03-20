from commons import directions
from location import Location


class CreateMonster:
    """

    :return:
    """

    def __init__(self, reader):

        self.unit = None
        self.timer = None
        self.location = None
        self.pos = None
        self.dir = None
        self.type = None
        self.frame = None
        self.phase = None
        self.pause = None
        self.weapon = None
        self.pocket = None

        self.decode(reader)

    def decode(self, reader):

        if not reader:
            return

        self.unit = reader.read_ubyte()
        self.timer = reader.read_ubyte()
        self.location = Location(reader)
        self.pos = reader.read_ubyte()
        self.dir = reader.read_byte()
        self.type = reader.read_ubyte()
        self.frame = reader.read_ubyte()
        self.phase = reader.read_ubyte()
        self.pause = reader.read_ubyte()
        self.pocket = reader.read_ushort()
        self.weapon = reader.read_ushort()

    def run(self, maze, assets):
        return "Create monster #{unit}, timer: {timer}, location: {location}, subpos: {pos}, dir: {dir}, " \
               "frame: {frame}, phase: {phase}, pause: {pause}, pocket: {pocket}, weapon: {weapon}".format(
            unit=self.unit, timer=self.timer, location=self.location, pos=self.pos, dir=directions[self.dir],
            frame=self.frame, phase=self.phase, pause=self.pause, pocket=self.pocket, weapon=self.weapon
        )
