from location import Location


class IsPartyAtLocation:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.code = None
        self.type = None
        self.flags = None
        self.location = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return
        self.code = reader.read_ubyte()

        if self.code == 0xF5:   # Count items
            self.type = reader.read_ushort()
            self.flags = reader.read_ubyte()

        else:   # Party position
            self.location = Location(reader)

    def run(self, maze, assets):

        if self.code == 0xF5:
            return "party inventory count of 0x{type:04X} flags: 0x{flags:02X}".format(
                type=self.type, flags=self.flags
                )
        else:
            return "party is at location {location}".format(location=self.location)
