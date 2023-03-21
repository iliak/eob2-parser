from location import Location


class IdentifyAllItems:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.location = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.location = Location(reader)

    def decode(self, maze, assets):

        return f"Identify all items at {self.location}"
