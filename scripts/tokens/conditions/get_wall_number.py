from location import Location


class GetWallNumber:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.location = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.location = Location(reader)

    def decode(self, tokens, maze, assets):

        return f"wall index at {self.location}"
