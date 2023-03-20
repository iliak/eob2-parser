
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

        self.target = reader.read_byte()
        self.points = reader.read_ubyte()

    def run(self, maze, assets):

        if self.target:
            return "Heal champion #{id} of {points} points".format(id=self.target, points=self.points)
        else:
            return "Heal team of {points} points".format(points=self.points)

