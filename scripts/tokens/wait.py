

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

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.delay = reader.read_ushort()

    def decode(self, maze, assets):

        return f"Wait {self.delay} ticks ({self.delay * 55} ms)"

