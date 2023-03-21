from commons import races


class HasRace:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.id = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.id = reader.read_ubyte()

    def run(self, maze, assets):

        return f"has race \"{races[self.id]}\""

