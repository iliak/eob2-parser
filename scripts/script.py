from scripts import tokens


class Script:
    """

    """
    opcodes = {
        0xFF: tokens.SetWall,
        0xFE: tokens.ChangeWall,
        0xFD: tokens.OpenDoor,
        0xFC: tokens.CloseDoor,
        0xFB: tokens.CreateMonster,
        0xFA: tokens.Teleport,
        0xF9: tokens.StealItem,
        0xF8: tokens.Message,
        0xF7: tokens.SetFlag,
        0xF6: tokens.Sound,
        0xF5: tokens.ClearFlag,
        0xF4: tokens.Heal,
        0xF3: tokens.Damage,
        0xF2: tokens.Goto,  # GoTo
        0xF1: tokens.End,
        0xF0: tokens.Return,
        0xEF: tokens.GoSub,  # GoSub
        0xEE: tokens.Condition,
        0xED: tokens.ConsumeItem,  # RemoveItem
        0xEC: tokens.ChangeLevel,
        0xEB: tokens.GiveXP,
        0xEA: tokens.NewItem,  # AddItem
        0xE9: tokens.Launcher,
        0xE8: tokens.Turn,
        0xE7: tokens.IdentifyAllItems,
        0xE6: tokens.Sequence,  # Encounter
        0xE5: tokens.Wait,
        0xE4: tokens.UpdateScreen,
        0xE3: tokens.Dialog,
        0xE2: tokens.SpecialEvent,
        0xD3: None,  # Cut scene
    }

    def __init__(self, reader):
        """

        """
        self.tokens = {}

        self.decompile(reader)

    def decompile(self, reader):
        """

        :return:
        """
        start = reader.offset
        length = reader.read_ushort()

        while reader.offset < start + length:

            offset = reader.offset - start
            opcode = reader.read_ubyte()
            type = self.opcodes.get(opcode)
            if type:
                token = type(reader)
                self.tokens[offset] = token
            else:
                print("###########[ERROR] unknown opcode: 0x{opcode:02X}".format(opcode=opcode))

    def run(self, maze, assets):
        return {f"0x{token:04X}": self.tokens[token].decode(maze, assets) for token in self.tokens}
