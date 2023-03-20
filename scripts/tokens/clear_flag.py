
class ClearFlag:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.type = None
        self.flag = None
        self.monster_id = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_byte()
        if self.type in [-17, -16]:  # Maze or global
            self.flag = reader.read_ubyte()

        elif self.type == -28:  # event
            pass

        elif self.type == -47:  # Party ??
            pass

    def run(self, maze, assets):

        if self.type == -17:
            return "Clear level flag {flag}".format(flag=self.flag)

        elif self.type == -16:
            return "Clear global flag {flag}".format(flag=self.flag)

        elif self.type == -28:
            return "Clear dialog result flag".format()

        elif self.type == -47:
            return "Clear 'Prevent rest' flag".format()
