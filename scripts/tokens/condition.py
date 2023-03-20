from .conditions import *


class Condition:
    """

    """

    def __init__(self, reader):
        """

        :param reader:
        """
        self.tokens = []
        self.target = None

        self.decode(reader)

    def decode(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        conditions = {
            0xFE: Comparator,
            0xFD: Comparator,
            0xFB: Comparator,
            0xF9: Comparator,
            0xF8: Comparator,
            0xF7: GetWallNumber,
            0xF5: IsItemAtLocation,
            0xF3: IsMonsterAtLocation,
            0xF1: IsPartyAtLocation,
            0xF0: GetGlobalFlag,
            0xEF: GetLevelFlag,
            0xEE: Else,  # ELSE GOTO
            0xED: GetPartyDirection,
            0xE9: GetWallSide,
            0xE7: GetPointerItem,
            0xE0: GetTriggerFlag,
            0xDF: ConditionDF,
            0xDD: HasRace,
            0xDC: HasClass,
            0xDB: RollDice,
            0xDA: IsPartyVisible,
            0xD7: ConditionD7,
            0xD2: ImmediateShort,
            0xCE: HasAlignment,
            0x01: PushTrue,
            0x00: PushFalse,
        }
        # "IF "
        while True:
            opcode = reader.read_ubyte()
            if opcode == 0xee:
                break

            type = conditions.get(opcode)
            if not type:
                token = PushValue(reader, opcode)
            else:
                token = type(reader)

            self.tokens.append(token)

        self.target = reader.read_ushort()
        i = 1

    def run(self, maze, assets):

        str = "If "
        for token in self.tokens:
            str += token.run(maze, assets) + '|'

        return str + ' else goto 0x{target:04X}'.format(target=self.target)
