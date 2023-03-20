
class GetPointerItem:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.action = None
        self.id = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.action = reader.read_ubyte()
        if self.action == 0xD0:
            self.id = reader.read_ubyte()
        elif self.action == 0xCF:
            self.id = reader.read_ubyte()

    def run(self, maze, assets):

        if self.action == 0xF5:
            return "hand item"
        elif self.action == 0xF6:
            return "hand item value"
        elif self.action == 0xE1:
            return "hand item type"
        elif self.action == 0xD0:
            return "hand item unidentified name id == #{value}".format(value=self.id)
        elif self.action == 0xCF:
            return "hand item identified name id == #{value}".format(value=self.id)
