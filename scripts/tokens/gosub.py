class GoSub:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.offset = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.offset = reader.read_ushort()

    def run(self, maze, assets):
        return f"GOSUB 0x{self.offset:04X}"
