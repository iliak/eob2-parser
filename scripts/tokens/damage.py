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

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.target = reader.read_ubyte()
        self.times = reader.read_ubyte()
        self.itemOrPips = reader.read_ubyte()
        self.mod = reader.read_ubyte()
        self.flags = reader.read_ubyte()
        self.savingThrowType = reader.read_ubyte()
        self.savingThrowEffect = reader.read_ubyte()

    def decode(self, maze, assets):
        target = 'team ' if self.target == 0xFF else ''
        return f"Damage {target}{self.times} time(s) with item {self.itemOrPips}, modifier: {self.mod}, flags: 0x{self.flags:02X}, " \
               f"savingThrowType: {self.savingThrowEffect}, savingThrowEffect: {self.savingThrowEffect}"
