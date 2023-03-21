
class SetGlobalFlag:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.flag = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.flag = reader.read_ubyte()

    def decode(self, tokens, maze, assets):

        return "set Global flag {flag}".format(flag=self.flag)
