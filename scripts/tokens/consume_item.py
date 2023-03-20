from location import Location


class ConsumeItem:
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

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_byte()
        if self.type != -1:
            self.location = Location(reader)

    def run(self, maze, assets):

        if self.type == -1:
            return "Consume hand item"
        else:
            return "Consume item of type {type} at {location}".format(type=self.type, location=self.location)

