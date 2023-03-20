
class Dice:
    """

    """
    def __init__(self, reader=None):
        self.rolls = 0
        self.sides = 0
        self.base = 0

        self.process(reader)

    def process(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.rolls = reader.read_ubyte()
        self.sides = reader.read_ubyte()
        self.base = reader.read_ubyte()

    def decode(self):
        return {
            'rolls': self.rolls,
            'sides': self.sides,
            'base': self.base,
        }

    def __str__(self):

        return "({rolls}d{sides})+{base}".format(rolls=self.rolls, sides=self.sides, base=self.base)
