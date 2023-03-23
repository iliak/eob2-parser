

class Encounter:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.cmd = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.cmd = reader.read_ubyte()

    def decode(self, maze, assets):

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
            return 'Encounter: Check password'
        elif self.cmd == 0xFE: #-2:
            return 'Encounter: Portal'
        elif self.cmd == 0xFD: #-3:
            return 'Encounter: Final scene...'

        return f"Encounter: NPC #{self.cmd}"
