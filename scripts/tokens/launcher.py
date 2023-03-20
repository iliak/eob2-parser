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

        self.type = reader.read_byte()
        self.item_id = reader.read_ushort()
        self.location = Location(reader)
        self.direction = reader.read_ubyte()
        self.sub_position = reader.read_ubyte()

    def run(self, maze, assets):

        if self.type == -33:
            return "Launching spell #{spell_id} from {location} facing {direction} at subpos {subpos}".format(
                spell_id=self.item_id, location=self.location, direction=directions[self.direction], subpos=self.sub_position
            )

        elif self.type == -20:
            return "Launching item #{item_id} from {location} facing {direction} at subpos {subpos}".format(
                item_id=self.item_id, location=self.location, direction=directions[self.direction], subpos=self.sub_position
            )

