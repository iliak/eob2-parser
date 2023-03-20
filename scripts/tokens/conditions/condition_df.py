
class ConditionDF:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.value = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        # self.value = reader.read_ubyte()

    def run(self, maze, assets):
        return "condition 0xDF()".format(value=self.value)

