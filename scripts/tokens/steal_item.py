from location import Location


class StealSmallItem:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.whom = None
        self.location = None
        self.sub_position = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.whom = reader.read_byte()
        self.location = Location(reader)
        self.sub_position = reader.read_ubyte()

    def run(self, maze, assets):

        if self.whom == -1:
            return "Steal small item and drop it at {location}:{subpos}".format(
                location=self.location, subpos=self.sub_position
            )
        else:
            return "Steal small item member: {member} and drop it at {location}:{subpos}".format(
                member=self.whom, location=self.location, subpos=self.sub_position
            )
