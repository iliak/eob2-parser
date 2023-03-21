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

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.offset = reader.read_ushort()

    def decode(self, maze, assets):
        return f"GoSub 0x{self.offset:04X}"
