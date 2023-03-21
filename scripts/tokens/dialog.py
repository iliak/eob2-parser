

class Dialog:
    """

    :return:
    """

    def __init__(self, reader):

        self.type = None
        self.picture_name = None
        self.x = None
        self.y = None
        self.rect = None
        self.flags = None
        self.text_id = None
        self.buttons = [None for i in range(6)]

        self.read(reader)

    def read(self, reader):

        if not reader:
            return

        self.type = reader.read_byte()

        if self.type == -45:    # Display a picture from a cps file
            self.picture_name = reader.read_string(13)
            self.rect = reader.read_ubyte()
            self.x = reader.read_ushort()
            self.y = reader.read_ushort()
            self.flags = reader.read_ushort()

        elif self.type == -44:  # Close dialog
            pass

        elif self.type == -43:  # Display background
            pass

        elif self.type == -42:  # Draw dialog box
            pass

        elif self.type == -40:  # Run dialog
            # vm->runDialogue(READ_LE_UINT16(pos),
            # READ_LE_UINT16(pos + 6) == 0xFFFF ? 2 : 3,
            # getString(READ_LE_UINT16(pos + 2)),
            # getString(READ_LE_UINT16(pos + 4)),
            # getString(READ_LE_UINT16(pos + 6)));
            self.text_id = reader.read_short()
            self.buttons[0] = reader.read_short()
            self.buttons[1] = reader.read_short()
            self.buttons[2] = reader.read_short()

        elif self.type == -8:  # Dialog text
            self.x = reader.read_ushort()
            self.y = reader.read_ushort()

    def decode(self, maze, assets):

        if self.type == -45:    # Display a picture from a cps file
            return "Draw sequence : '{picture}', rect: {rect}, X: {x}, Y: {y}, flags: 0x{flags:04X}".format(
                x=int(self.x / 8), y=self.y, picture=self.picture_name, flags=self.flags, rect=self.rect)

        elif self.type == -44:  # Close dialog
            return "Close dialog"

        elif self.type == -43:  # Init dialog sequence
            return "Init dialog sequence"

        elif self.type == -42:  # Draw dialog box
            return "Draw dialog box"

        elif self.type == -40:  # Run dialog
            return "Run dialog '{txt}', Buttons: ['{b1}', '{b2}', '{b3}']".format(
                text_id=self.text_id,
                txt=assets['texts'][self.text_id - 1],
                b1=maze.messages[self.buttons[0]] if self.buttons[0] != -1 else '',
                b2=maze.messages[self.buttons[1]] if self.buttons[1] != -1 else '',
                b3=maze.messages[self.buttons[2]] if self.buttons[2] != -1 else '',
            )

        elif self.type == -8:  #
            return f"Print dialog text: '{assets['texts'][self.x - 1]}' , Text #{self.y}: '{maze.messages[self.y]}'"

