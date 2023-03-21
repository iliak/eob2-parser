from dice import Dice


class RollDice:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.dice = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        self.dice = Dice(reader)

    def run(self, maze, assets):

        return "dice {dice}".format(dice=self.dice)

