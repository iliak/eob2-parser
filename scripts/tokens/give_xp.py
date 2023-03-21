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

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_ubyte()
        self.amount = reader.read_ushort()

    def run(self, maze, assets):

        if self.type == 0xE2:  # -30:
            return f"Give {self.amount} XP to the team [type: {self.type}]"
