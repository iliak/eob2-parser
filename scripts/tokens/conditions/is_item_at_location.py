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

        if self.type == 0xFF00:
            return f"item at {self.location}"
        else:
            return f"item of type 0x{self.type:04X} at {self.location}"
