class Goto:
    """

    :return:
    """

    def __init__(self, reader):
        self.offset = None
        self.decode(reader)

    def decode(self, reader):
        if not reader:
            return

        self.offset = reader.read_ushort()

    def run(self, maze, assets):
        return f"Goto 0x{self.offset:04X}"
