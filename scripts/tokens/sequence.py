

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

        self.cmd = reader.read_ubyte()

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
        if self.cmd == 0xFF: #-1:
            return 'Sequence: Check password'
        elif self.cmd == 0xFE: #-2:
            return 'Sequence: Portal'
        elif self.cmd == 0xFD: #-3:
            return 'Sequence: Final scene...'

        return f"Sequence: NPC #{self.cmd}"
