from commons import directions
from location import Location


class ChangeLevel:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.cmd = None
        self.index = None
        self.level = None
        self.sub = None
        self.location = None
        self.direction = None
        self.monster = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.cmd = reader.read_byte()
        self.index = reader.read_byte()

        if self.cmd == -27:
            self.sub = reader.read_byte()
            self.location = Location(reader)
            self.direction = reader.read_byte()

        else:
            self.level = reader.read_byte()
            self.monster = reader.read_byte(13)

    def run(self, maze, assets):

        if self.cmd == -27:
            return "Entering to level {level}, sub level {sub} at {location} facing to {direction}".format(
                level=self.index, sub=self.sub, location=self.location, direction=directions[self.direction])

        else:
            return "Loading monster shape: {shape}, id: {id} type: {type}".format(
                shape=self.monster[0], id=self.level, type=self.index)
