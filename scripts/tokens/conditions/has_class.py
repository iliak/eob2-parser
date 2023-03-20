from commons import classes


class HasClass:
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

        self.id = reader.read_byte()

    def run(self, maze, assets):

        return "check if character with class {name} is present"\
            .format(name=classes[self.id])

