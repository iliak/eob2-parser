from .conditions import *


class Eval:
    """

    See https://github.com/scummvm/scummvm/blob/master/engines/kyra/script/script_eob.cpp
    """
    conditions = {
        0xFF: Equals,
        0xFE: Differents,
        0xFD: MoreThan,
        0xFC: MoreEqualsThan,
        0xFB: LessThan,
        0xFA: LessEqualsThan,
        0xF9: And,
        0xF8: Or,
        0xF7: GetWallNumber,
        0xF5: ItemCountAtLocation,
        0xF3: IsMonsterAtLocation,  # TestBlockFlag
        0xF2: IsItemAtLocation,
        0xF1: IsPartyAtLocation,
        0xF0: GetGlobalFlag,
        0xEF: GetLevelFlag,
        0xEE: Else,
        0xED: GetPartyDirection,
        0xE9: GetWallSide,
        # 0xE8: GetTeamSize,
        0xE7: GetPointerItem,
        0xE4: DialogResult,
        0xE0: GetTriggerFlag,
        0xDF: OnSpell,
        0xDD: HasRace,
        0xDC: HasClass,
        0xDB: RollDice,
        0xDA: IsPartyVisible,
        0xD7: OnBash,
        0xD2: ImmediateShort,
        0xCE: HasAlignment,
        0x68: Condition68,
        0x02: Condition02,
        0x01: PushTrue,
        0x00: PushFalse,
    }

    def __init__(self, reader):
        """

        :param reader:
        """
        self.tokens = []
        self.goto = None

        self.read(reader)

    def read(self, reader):
        """

        :param reader:
        :return:
        """

        if not reader:
            return

        # "IF "
        while True:
            opcode = reader.read_ubyte()
            if opcode == 0xee:
                break

            type = self.conditions.get(opcode)
            if not type:
                token = UnknownCondition(reader, opcode)
            else:
                token = type(reader)

            self.tokens.append(token)

        self.goto = reader.read_ushort()

    def decode(self, maze, assets):

        tokens = list(self.tokens)
        token = tokens.pop()

        try:
            decoded = token.decode(tokens, maze, assets)
            msg = f"If {decoded} else goto 0x{self.goto:04X}"
        except IndexError as e:
            msg = f"[ERROR]###################### {e}"

        return msg
