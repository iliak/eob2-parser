
class SetGlobalFlag:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.flag = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.flag = reader.read_ubyte()

    def run(self, maze, assets):

        return "set Global flag {flag}".format(flag=self.flag)
