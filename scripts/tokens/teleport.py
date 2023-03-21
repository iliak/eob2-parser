from location import Location


class Teleport:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.type = -1  # a action
        self.source = -1
        self.destination = -1
        self.item_type = -1  # b item type
        self.src_level = -1  # c source block
        self.dst_level = -1  # d target block ?
        self.src_blk = -1  # e Source level ?
        self.dst_blk = -1  # f target level ?
        self.sub = -1
        # self.tmp = -1
        # self.tmp2 = -1
        # self.payload = []

        self.read(reader)

    def read(self, reader):
        """
        BOGUS extra data not handled
        :param reader:
        :return:
        """
        self.type = reader.read_ubyte()

        if self.type == 0xE1:  # -31:
            self.item_type = reader.read_ushort()

        self.source = Location(reader)

        if self.type == 0xF5:  # -11:    # Move item
            self.src_level = reader.read_ubyte()
            self.sub = reader.read_ubyte()
            if self.sub == 0xe5:
                self.dst_level = reader.read_ubyte()
                self.dst_blk = Location(reader)
            elif self.sub == 0xeb:
                self.dst_blk = Location(reader)
            else:
                self.payload = reader.read_ubyte(4)

        elif self.type == 0xE1:  # -31:  # Move item by type
            self.src_blk = Location(reader)
            self.dst_blk = Location(reader)

        elif self.type == 0xF3:  # -13:  # Move monster
            self.destination = Location(reader)

        elif self.type == 0xE8:  # -24:  # Move party
            self.destination = Location(reader)

    def decode(self, maze, assets):

        if self.type == 0xE8:  # -24:
            return "Teleport team to {dest}".format(dest=self.destination)

        elif self.type == 0xF3:  # -13:
            return "Teleport monsters from {src} to {dest}".format(src=self.source, dest=self.destination)

        elif self.type == 0xF5:  # -11:
            if self.sub == 0xE5:
                return f"Teleport (0xF5) items from level {self.src_level}@{self.source} to level {self.dst_level}@{self.dst_blk}"
            elif self.sub == 0xEB:
                return f"Teleport (0xF5) items in current level from {self.source} to {self.dst_blk}"
            else:
                return f"Teleport (0xF5) ERROR ### #0x{self.type:02X} sub 0x{self.sub:02X} payload: {[f'0x{x:02X}' for x in self.payload]}"

        elif self.type == 0xE1:  # -31:
            return "Teleport item of type {item_type} from {source} to {dest}".format(
                item_type=self.item_type, dest=self.dst_blk, source=self.src_blk)

        else:
            return f"Teleport ### #{self.type:02X}"
