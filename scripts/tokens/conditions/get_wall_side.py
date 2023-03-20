from commons import directions
from location import Location


class GetWallSide:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.side = None
        self.location = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.side = reader.read_ubyte()
        self.location = Location(reader)

    def run(self, maze, assets):

        return "wall side {side} at {location}".format(side=directions[self.side], location=self.location)

