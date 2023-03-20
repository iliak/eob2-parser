


class Call:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.target = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.target = reader.read_ushort()

    def run(self, maze, assets):

        return "Call 0x{target:04X}" \
            .format(target=self.target)

