from commons import directions
from location import Location


class SetWall:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.type = None
        self.location = None
        self.to = None
        self.side = None
        self.direction = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_byte()

        if self.type == -9:    # All sides
            self.location = Location(reader)
            self.to = reader.read_ubyte()

        elif self.type == -23:     # one side
            self.location = Location(reader)
            self.side = reader.read_ubyte()
            self.to = reader.read_ubyte()

        elif self.type == -19:     # change party direction
            self.direction = reader.read_ubyte()

    def run(self, maze, assets):

        if self.type == -9:
            return "Set walls at {location} all sides to {to:02}".format(location=self.location, to=self.to)

        elif self.type == -23:
            return "Set wall at {location} side {side} to {to:02}".format(
                location=self.location, side=self.side, to=self.to)

        elif self.type == -19:
            return "Set party direction to {direction}".format(direction=directions[self.direction])

