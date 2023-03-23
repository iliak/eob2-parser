
class GetPointerItem:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.action = None
        self.id = None

        self.read(reader)

    def read(self, reader):
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

    def decode(self, tokens, maze, assets):

        if self.action == 0xF5:
            return "pointer item number"
        elif self.action == 0xF6:
            return "pointer item value"
        elif self.action == 0xE1:
            return "pointer item type"
        elif self.action == 0xD0:
            return "pointer item unidentified name id == #{value}".format(value=self.id)
        elif self.action == 0xCF:
            return "pointer item identified name id == #{value}".format(value=self.id)
