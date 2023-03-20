from commons import races


class HasRace:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.id = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.id = reader.read_ubyte()

    def run(self, maze, assets):

        return "check if character with race {race} is present".format(race=races[self.id])

