from location import Location


class ItemCountAtLocation:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.type = None
        self.location = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.type = reader.read_ushort()
        self.location = Location(reader)

    def decode(self, tokens, maze, assets):

        return f"count items of type 0x{self.type:04X} at {self.location}"
