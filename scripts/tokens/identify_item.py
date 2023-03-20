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

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.location = Location(reader)

    def run(self, maze, assets):

        return "Identify all items at {location}".format(
            location=self.location
        )
