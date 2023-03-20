
class Damage:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.target = None
        self.times = None
        self.itemOrPips = None
        self.mod = None
        self.flags = None
        self.savingThrowType = None
        self.savingThrowEffect = None

        self.vs_small = None
        self.vs_big = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.target = reader.read_byte()
        self.times = reader.read_byte()
        self.itemOrPips = reader.read_byte()
        self.mod = reader.read_byte()
        self.flags = reader.read_byte()
        self.savingThrowType = reader.read_byte()
        self.savingThrowEffect = reader.read_byte()

    def run(self, maze, assets):

        target = 'team ' if self.target == -1 else ''
        return "Damage {target}{times} time(s) with item {item}, modifier: {mod}, flags: 0x{flags:02X}, " \
               "savingThrowType: {type}, savingThrowEffect: {effect}".format(
            target=target, times=self.times, item=self.itemOrPips, mod=self.mod, flags=self.flags,
            type=self.savingThrowType, effect=self.savingThrowEffect
        )

