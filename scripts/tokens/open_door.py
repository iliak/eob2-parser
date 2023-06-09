from location import Location


class OpenDoor:
    """

    :param reader:
    :return:
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

    def decode(self, maze, assets):

        return f"Open door at {self.location}"
