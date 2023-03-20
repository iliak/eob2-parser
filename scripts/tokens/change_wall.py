from location import Location


class ChangeWall:
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
        self.model = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_byte()
        self.location = Location(reader)

        if self.type == -9:   # All side
            self.to = reader.read_ubyte()
            self.model = reader.read_ubyte()

        elif self.type == -23:     # One side
            self.side = reader.read_ubyte()
            self.to = reader.read_ubyte()
            self.model = reader.read_ubyte()

        elif self.type == -22:     # Door
            pass

    def run(self, maze, assets):

        if self.type == -9:
            return "Change wall at {location} all sides from: {model} to: {to}".format(
                location=self.location, model=self.model, to=self.to)

        elif self.type == -23:
            return "Change wall at {location} side: {side} from: {model} to: {to}".format(
                location=self.location, side=self.side, model=self.model, to=self.to)

        elif self.type == -22:
            return "Process door switch at {location}".format(
                location=self.location)

