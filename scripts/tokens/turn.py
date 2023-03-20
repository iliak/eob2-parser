from commons import directions


class Turn:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.cmd = None
        self.dir = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.cmd = reader.read_byte()
        self.dir = reader.read_ubyte()
        i = 1

    def run(self, maze, assets):

        if self.cmd == -15:
            return "Change party direction to {dir}".format(dir=directions[self.dir])

        elif self.cmd == -11:
            return "Change flying item direction to {dir}".format(dir=directions[self.dir])

        else:
            return '[ERROR] Turn'

