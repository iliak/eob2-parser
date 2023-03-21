class GiveXP:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.type = None
        self.amount = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_ubyte()
        self.amount = reader.read_ushort()

    def decode(self, maze, assets):

        if self.type == 0xE2:  # -30:
            return f"Give {self.amount} XP to the team [type: {self.type}]"
        else:
            return f"Give XP ERROR"
