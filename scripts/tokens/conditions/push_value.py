class PushValue:
    """
    BOGUS
    """

    def __init__(self, reader=None, value=None):
        """

        :param reader:
        """

        self.value = value
        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        # self.value = reader.read_ushort()

    def run(self, maze, assets):
        # if self.value <= 128:
        return "push 0x{value:04X}".format(value=self.value)
        # else:
        #     return "####0x{value:02X} ({value})".format(value=self.value)

