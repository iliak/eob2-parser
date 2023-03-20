class MenuChoice:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.type = None
        self.value = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.type = reader.read_ubyte()
        self.value = reader.read_ushort()

    def run(self, maze, assets):
        return "push menu choice, Push 0x{value:04X}".format(value=self.value)
