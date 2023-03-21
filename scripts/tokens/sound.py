from location import Location


class Sound:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.id = None
        self.location = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.id = reader.read_ubyte()
        self.location = Location(reader)

    def run(self, maze, assets):

        if self.location.x or self.location.y:
            return f"Environmental sound {self.id} at {self.location}"
        else:
            return f"Sound {self.id}"

