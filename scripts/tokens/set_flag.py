
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

        self.read(reader)

    def read(self, reader):
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

    def decode(self, maze, assets):

        if self.type == -17:       # -17 level
            return f"Set level flag {self.flag}"

        if self.type == -16:       # -16 global
            return f"Set global flag {self.flag}"

        elif self.type == -13:     # -13 monster
            return f"Set monster {self.monster_id} flag {self.flag}"

        elif self.type == -28:
            return "Set dialog result to 1"

        elif self.type == -47:
            return "Set 'Prevent rest' flag"

