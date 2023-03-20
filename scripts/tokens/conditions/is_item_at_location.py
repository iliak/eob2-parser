from location import Location


class IsItemAtLocation:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.type = None
        self.location = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.type = reader.read_ushort()
        self.location = Location(reader)

    def run(self, maze, assets):

        if self.type == 0xFF00:
            return "maze count items at {location}".format(
                location=self.location
            )
        else:
            return "maze count items of type 0x{type:04X} at {location}".format(
                type=self.type, location=self.location
            )


