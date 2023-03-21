from commons import directions
from location import Location


class Launcher:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.type = None
        self.item_id = None
        self.location = None
        self.direction = None
        self.sub_position = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.type = reader.read_ubyte()
        self.item_id = reader.read_ushort()
        self.location = Location(reader)
        self.direction = reader.read_ubyte()
        self.sub_position = reader.read_ubyte()

    def run(self, maze, assets):

        if self.type == 0xDF:  # -33:
            return f"Launching spell #{self.item_id} from {self.location} facing {directions[self.direction]} at subpos {self.sub_position}"

        elif self.type == 0xEC:  # -20:
            return f"Launching item #{self.item_id} from {self.location} facing {directions[self.direction]} at subpos {self.sub_position}"
