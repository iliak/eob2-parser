

class Sequence:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.cmd = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.cmd = reader.read_byte()

    def run(self, maze, assets):

        """
        nightmare
        kheldran
        dran dragon transformation
        finale
        credits
        intro
        xdeath
        portal

        :return:
        """
        if self.cmd == -1:
            return 'Sequence: Check password'
        elif self.cmd == -2:
            return 'Sequence: Portal'
        elif self.cmd == -3:
            return 'Sequence: Final scene...'

        return "Sequence: NPC #{id}".format(
            id=self.cmd
        )
