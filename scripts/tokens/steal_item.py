from location import Location


class StealItem:
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

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.whom = reader.read_ubyte()
        self.location = Location(reader)
        self.sub_position = reader.read_ubyte()

    def decode(self, maze, assets):

        if self.whom == 0xFF: #-1:
            return f"Steal item and drop it at {self.location}:{self.sub_position}"
        else:
            return f"Steal item member: {self.whom} and drop it at {self.location}:{self.sub_position}"
