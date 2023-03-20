
class Jump:
    """

    :return:
    """

    def __init__(self, reader):

        self.addr = None
        self.decode(reader)

    def decode(self, reader):

        if not reader:
            return

        self.addr = reader.read_ushort()

    def run(self, maze, assets):
        return "Jump to [0x{target:04X}]".format(target=self.addr)

