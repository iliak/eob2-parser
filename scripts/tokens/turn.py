from commons import directions


class Turn:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.cmd = None
        self.dir = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.cmd = reader.read_ubyte()
        self.dir = reader.read_ubyte()

    def decode(self, maze, assets):

        if self.cmd == 0xF1:  # -15:
            return f"Change party direction to {directions[self.dir]}"

        elif self.cmd == 0xF5:  # -11:
            return f"Change flying item direction to {directions[self.dir]}"

        else:
            return f'[ERROR] Turn 0x{self.cmd:02X}'
