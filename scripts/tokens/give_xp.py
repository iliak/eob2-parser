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

        self.type = reader.read_byte()
        self.amount = reader.read_ushort()

    def run(self, maze, assets):

        if self.type == -30:
            return "Give {amount} XP to the team [type: {type}]".format(
                amount=self.amount, type=self.type
            )
