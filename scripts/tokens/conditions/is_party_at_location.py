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

        self.read(reader)

    def read(self, reader):
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

    def decode(self, tokens, maze, assets):

        if self.code == 0xF5:
            return "team inventory count of 0x{type:04X} flags: 0x{flags:02X}".format(
                type=self.type, flags=self.flags
                )
        else:
            return "team at {location}".format(location=self.location)
