from commons import ItemSlotFlags, ItemFlags, ProfessionFlags, HandFlags
from dice import Dice
from tools.reader import BinaryReader


def itemtypes_decode():
    """

    types:
     47 => rings
     31 => eatable/food
    """
    item_types = []
    with BinaryReader('data/ITEMTYPE.DAT') as reader:
        count = reader.read_ushort()
        for i in range(count):
            type = {
                # At which position in inventory it is allowed to be put. See InventoryUsage
                'slots':           str(ItemSlotFlags(reader.read_ushort())),
                'flags':           str(ItemFlags(reader.read_ushort())),
                'armor_class':     reader.read_ubyte(),  # Adds to armor class
                'allowed_classes': str(ProfessionFlags(reader.read_ubyte())),  # Allowed for this profession. See ClassUsage
                'required_hand':   str(HandFlags(reader.read_ubyte())),  # Allowed for this hand
                'damage_vs_small': str(Dice(reader)),
                'damage_vs_big':   str(Dice(reader)),
                # 'damage_incs': reader.read_ubyte(),
                'unknown':         reader.read_ubyte(),
                'extra':           reader.read_ushort(),
            }

            item_types.append(type)

    return item_types
    # print("Item types :", json.dumps(item_types, indent=2, sort_keys=True))
