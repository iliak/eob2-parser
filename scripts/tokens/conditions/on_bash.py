

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
        if self.value == 0xDC:
            return f"last used item extra properties"
        elif self.value == 0xE1:
            return f"last used item type"
        elif self.value == 0xF5:
            return f"last used item value"
        elif self.value == 0xF6:
            return f"last used item"
