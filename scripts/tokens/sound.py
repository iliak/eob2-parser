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
            return "Play environmental sound {id} at {location}".format(id=self.id, location=self.location)
        else:
            return "Play sound {id}".format(id=self.id)

