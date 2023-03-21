from location import Location


class IsMonsterAtLocation:
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

        # TODO: Location is wrong...
        self.location = Location(reader)

    def decode(self, tokens, maze, assets):
        return f"monster at {self.location}"
