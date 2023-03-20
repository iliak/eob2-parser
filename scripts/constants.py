from enum import Enum


class ScriptTokens(Enum):
    TOKEN_SET_WALL = 0xff,
    TOKEN_CHANGE_WALL = 0xfe,
    TOKEN_OPEN_DOOR = 0xfd,
    TOKEN_CLOSE_DOOR = 0xfc,
    TOKEN_CREATE_MONSTER = 0xfb,
    TOKEN_TELEPORT = 0xfa,
    TOKEN_STEAL_SMALL_ITEMS = 0xf9,
    TOKEN_MESSAGE = 0xf8,
    TOKEN_SET_FLAG = 0xf7,
    TOKEN_SOUND = 0xf6,
    TOKEN_CLEAR_FLAG = 0xf5,
    TOKEN_HEAL = 0xf4,
    TOKEN_DAMAGE = 0xf3,
    TOKEN_JUMP = 0xf2,
    TOKEN_END = 0xf1,
    TOKEN_RETURN = 0xf0,
    TOKEN_CALL = 0xef,
    TOKEN_CONDITIONAL = 0xee,
    TOKEN_CONSUME = 0xed,
    TOKEN_CHANGE_LEVEL = 0xec,
    TOKEN_GIVE_XP = 0xeb,
    TOKEN_NEW_ITEM = 0xea,
    TOKEN_LAUNCHER = 0xe9,
    TOKEN_TURN = 0xe8,
    TOKEN_IDENTIFY_ITEMS = 0xe7,
    TOKEN_ENCOUNTER = 0xe6,
    TOKEN_WAIT = 0xe5,