from location import Location


class IsMonsterAtLocation:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.location = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return
        self.location = Location(reader)

    def run(self, maze, assets):

        return "monster count at {location}".format(location=self.location)
