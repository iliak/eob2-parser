from location import Location


class NewItem:
    """

    :param reader:
    :return:
    """

    def __init__(self, reader):
        """

        :param reader:
        """

        self.type = None
        self.location = None
        self.subpos = None
        self.flags = None
        self.item_id = None
        self.item_value = None
        self.item_flag = None
        self.item_icon = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """
        if not reader:
            return

        self.item_id = reader.read_ushort()
        self.location = Location(reader)
        self.subpos = reader.read_ubyte()
        self.flags = reader.read_ubyte()

        if self.flags & 1 == 1:
            self.item_value = reader.read_ubyte()
        if self.flags & 2 == 2:
            self.item_flag = reader.read_ubyte()
        if self.flags & 4 == 4:
            self.item_icon = reader.read_ubyte()

    def decode(self, maze, assets):

        if self.location.value == 0xFF: #-1:
            return "New hand item id: {item_id} (value {value}, flags: {flags} 0x{flags:02x}, icon: {icon}]".format(
                item_id=self.item_id, value=self.item_value, flags=self.flags, icon=self.item_icon)

        elif self.location.value == 0xFE: #-2:
            return "New item #{item_id} on current block (value {value}, flags: {flags} 0x{flags:02x}, icon: {icon}]".format(
                item_id=self.item_id, value=self.item_value, flags=self.flags, icon=self.item_icon)

        else:
            return "New item #{item_id} at {location}, sub: {sub} flags: 0x{flags:02x}".format(
                item_id=self.item_id, location=self.location, sub=self.subpos, flags=self.flags)
