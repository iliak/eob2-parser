class Goto:
    """

    :return:
    """

    def __init__(self, reader):
        self.offset = None
        self.read(reader)

    def read(self, reader):
        if not reader:
            return

        self.offset = reader.read_ushort()

    def decode(self, maze, assets):
        return f"Goto 0x{self.offset:04X}"
