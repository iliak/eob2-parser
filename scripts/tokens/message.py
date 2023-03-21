class Message:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.message_id = None
        self.color = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.message_id = reader.read_ushort()
        self.color = reader.read_ushort()

    def decode(self, maze, assets):
        return f"Message '{maze.messages[self.message_id]}' color: {self.color}"
