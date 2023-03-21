from dice import Dice


class RollDice:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.dice = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.dice = Dice(reader)

    def decode(self, tokens, maze, assets):

        return "dice {dice}".format(dice=self.dice)

