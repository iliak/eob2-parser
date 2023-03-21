
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

        self.read(reader)

    def read(self, reader):
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

    def decode(self, maze, assets):

        if self.type == -17:
            return f"Clear level flag {self.flag}"

        elif self.type == -16:
            return f"Clear global flag {self.flag}"

        elif self.type == -28:
            return "Clear dialog result flag"

        elif self.type == -47:
            return "Clear 'Prevent rest' flag"
