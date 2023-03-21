class ImmediateShort:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.value = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.value = reader.read_ushort()

    def decode(self, tokens, maze, assets):
        return f"0x{self.value:04X}"

