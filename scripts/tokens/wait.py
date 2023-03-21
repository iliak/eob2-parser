

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

        return f"Wait {self.delay} ticks ({self.delay * 55} ms)"

