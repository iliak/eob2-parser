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

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.side = reader.read_ubyte()
        self.location = Location(reader)

    def decode(self, tokens, maze, assets):

        return f"{directions[self.side]} wall side at {self.location}"

