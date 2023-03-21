
class Heal:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.target = None
        self.points = 0

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.target = reader.read_ubyte()
        self.points = reader.read_ubyte()

    def run(self, maze, assets):

        if self.target:
            return f"Heal champion #{self.target} of {self.points} points"
        else:
            return f"Heal team of {self.points} points"

