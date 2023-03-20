
class SetFlag:
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
        if self.type in [-17, -16]:       # Maze or global
            self.flag = reader.read_ubyte()

        elif self.type == -13:     # monster
            self.monster_id = reader.read_ubyte()
            self.flag = reader.read_ubyte()

        elif self.type == -28:     # event
            pass

        elif self.type == -47:     # Party can't sleep ??
            pass

    def run(self, maze, assets):

        if self.type == -17:       # -17 level
            return "Set level flag {flag}".format(flag=self.flag)

        if self.type == -16:       # -16 global
            return "Set global flag {flag}".format(flag=self.flag)

        elif self.type == -13:     # -13 monster
            return "Set monster {monster} flag {flag}".format(monster=self.monster_id, flag=self.flag)

        elif self.type == -28:
            return "Set dialog result to 1"

        elif self.type == -47:
            return "Set 'Prevent rest' flag".format()

