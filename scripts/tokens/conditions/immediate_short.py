class ImmediateShort:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.value = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.value = reader.read_ushort()

    def run(self, maze, assets):
        return "value 0x{value:04X}".format(value=self.value)
