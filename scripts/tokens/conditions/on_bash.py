

class OnBash:
    """
    on thrown item ?
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.value = None
        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        self.value = reader.read_ubyte()

    def decode(self, tokens, maze, assets):
        return f"on bash(0x{self.value:02X})"
