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

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_ubyte()
        if self.type != 0xFF:
            self.location = Location(reader)

    def decode(self, maze, assets):

        if self.type == 0xFF:
            return "Consume hand item"
        else:
            return f"Consume item of type {self.type} at {self.location}"

