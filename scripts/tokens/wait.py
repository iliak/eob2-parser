

class Wait:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.delay = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.delay = reader.read_ushort()

    def run(self, maze, assets):

        return "Wait {delay} ticks ({ms} ms)".format(delay=self.delay, ms=self.delay * 55)

