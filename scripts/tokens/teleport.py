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

        self.type = -1        # a action
        self.source = -1
        self.destination = -1
        self.item_type = -1     # b item type
        self.src_level = -1     # c source block
        self.dst_level = -1     # d target block ?
        self.src_blk = -1       # e Source level ?
        self.dst_blk = -1       # f target level ?
        self.sub = -1
        # self.tmp = -1
        # self.tmp2 = -1
        # self.payload = []

        self.decode(reader)

    def decode(self, reader):
        """
        BOGUS extra data not handled
        :param reader:
        :return:
        """
        self.type = reader.read_byte()

        if self.type == -31:
            self.item_type = reader.read_ushort()

        self.source = Location(reader)

        if self.type == -11:    # Move item
            self.src_level = reader.read_byte()
            self.sub = reader.read_ubyte()
            if self.sub == 0xe5:
                self.dst_level = reader.read_byte()
                self.dst_blk = Location(reader)
            elif self.sub == 0xeb:
                self.dst_blk = Location(reader)
            else:
                self.payload = reader.read_ubyte(4)

        elif self.type == -31:  # Move item by type
            self.src_blk = Location(reader)
            self.dst_blk = Location(reader)

        elif self.type == -13:  # Move monster
            self.destination = Location(reader)

        elif self.type == -24:  # Move party
            self.destination = Location(reader)

        i = 1

    def run(self, maze, assets):

        if self.type == -24:
            return "Teleport team to {dest}".format(dest=self.destination)

        elif self.type == -13:
            return "Teleport monsters from {src} to {dest}".format(src=self.source, dest=self.destination)

        elif self.type == -11:
            # return "Teleport (-11) items tmp: 0x{tmp:02X} src_level: {src_level} payload: [{payload}]".format(
            #     src_level=self.src_level, tmp=self.tmp, payload=''.join("0x{:02X} ".format(x) for x in self.payload)
            # )

            if self.sub == 0xe5:
                return "Teleport (-11) items from level {src_level}:{source} to level {dst_level}:{dst_blk}".format(
                    src_level=self.src_level, source=self.source, dst_level=self.dst_level, dst_blk=self.dst_blk,
                )
            elif self.sub == 0xeb:
                return "Teleport (-11) items in current level from {source} to {dst_blk}".format(
                    source=self.source, dst_blk=self.dst_blk,
                )
            else:
                return "Teleport (-11) ERROR ### #{id} sub {sub} payload: {payload}".format(
                    id=self.type, sub=self.sub, payload=''.join("0x{:02X} ".format(x) for x in self.payload))

        elif self.type == -31:
            return "Teleport item of type {item_type} from {source} to {dest}".format(
                item_type=self.item_type, dest=self.dst_blk, source=self.src_blk)

        else:
            return "Teleport ### #{id}".format(id=self.type)
