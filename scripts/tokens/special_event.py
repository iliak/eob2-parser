
class SpecialEvent:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.id = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.id = reader.read_ushort()

    def decode(self, maze, assets):

        if self.id == 0:
            return "Special event: lightning"
        elif self.id == 1:
            return "Special event: character selection dialog"
        elif self.id == 2:
            return "Special event: character level gain dialog"
        elif self.id == 3:
            return "Special event: character resurrection dialog"
        elif self.id == 4:
            return "Special event: new party member dialog"
        elif self.id == 5:
            return "Special event: steal items (type: 46, value:5 & 6)"
        elif self.id == 6:
            return "Special event: clear screen"
