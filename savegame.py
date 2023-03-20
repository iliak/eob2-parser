from commons.champion import Champion
from commons import races, classes, alignments, directions, ItemSlotFlags, ItemFlags, ProfessionFlags, HandFlags
from dice import Dice
from location import Location
from monster import Monster
from tools.reader import BinaryReader


class Savegame:
    """

    """

    def __init__(self, filename, assets):
        self._filename = filename
        self.champions = []

        with BinaryReader(filename) as reader:
            self.name = reader.read_string(20)

            # Champions
            for i in range(6):
                champion = Champion()
                champion.id = reader.read_ubyte()
                champion.flags = reader.read_ubyte()
                champion.name = reader.read_string(11)
                champion.strength = {
                    "current": reader.read_byte(),
                    "max":     reader.read_byte()
                }
                champion.strength_extra = {
                    "current": reader.read_byte(),
                    "max":     reader.read_byte()
                }

                champion.intelligence = reader.read_byte(2)
                champion.wisdom = reader.read_byte(2)
                champion.dexterity = reader.read_byte(2)
                champion.constitution = reader.read_byte(2)
                champion.charisma = reader.read_byte(2)
                champion.hitpoint = reader.read_short(2)
                champion.armorclass = reader.read_byte(1)
                champion.disabled_slots = reader.read_byte()

                champion.race = races[reader.read_byte()]
                champion.class_ = classes[reader.read_byte()]
                champion.alignment = alignments[reader.read_byte()]
                champion.portrait = reader.read_byte()
                champion.food = reader.read_byte()
                champion.level = reader.read_byte(3)

                champion.experience = reader.read_uint(3)

                champion.pad_01 = reader.read_ubyte(4)

                champion.mage_spells = reader.read_byte(80)
                champion.cleric_spells = reader.read_byte(80)
                champion.mage_spells_available_flags = reader.read_ushort()

                champion.pad_02 = reader.read_ushort(1)

                champion.hand_left = reader.read_ushort()
                champion.hand_right = reader.read_ushort()
                champion.backpack = reader.read_ushort(14)
                champion.quiver = reader.read_ushort()
                champion.armor = reader.read_ushort()
                champion.wrists = reader.read_ushort()
                champion.helmet = reader.read_ushort()
                champion.necklace = reader.read_ushort()
                champion.boots = reader.read_ushort()
                champion.belt = reader.read_ushort(3)
                champion.rings = reader.read_ushort(2)

                champion.timers = reader.read_uint(10)
                champion.events = reader.read_ubyte(10)
                champion.effects_remainder = reader.read_ubyte(4)
                champion.effect_flags = reader.read_uint()

                champion.damage_taken = reader.read_byte()
                champion.slot_status = reader.read_byte(5)

                champion.pad_03 = reader.read_ubyte(6)

                self.champions.append(champion)

            # Game states
            assert reader.offset == 2090
            self.current_level = reader.read_ushort()
            self.sub_position = reader.read_short()
            self.position = Location(reader)
            self.direction = directions[reader.read_ushort()]
            self.item_in_hand = reader.read_ushort()
            self.has_tmp_data = reader.read_ushort()
            self.party_effect_flags = reader.read_ushort()
            self.pad_02 = reader.read_byte()
            self.prevent_rest = reader.read_byte()
            self.state_flags = reader.read_ushort(18)
            self.pad_03 = reader.read_byte(40)

            # items
            self.items = []
            item_names = assets['item_names']
            assert reader.offset == 2182
            for i in range(600):
                item = {
                    "name_unidentified": item_names[reader.read_ubyte()],
                    "name":              item_names[reader.read_ubyte()],
                    "flags":             reader.read_ubyte(),
                    "icon":              reader.read_byte(),
                    "type":              reader.read_byte(),
                    "position":          reader.read_byte(),
                    "location":          Location(reader),
                    "next":              reader.read_short(),
                    "previous":          reader.read_short(),
                    "level":             reader.read_ubyte(),
                    "value":             reader.read_byte(),
                }
                self.items.append(item)

            # Levels
            self.levels = []
            for id in range(17):
                level = {
                    "walls_encoded": reader.read_ubyte(1200)
                }
                # level['walls'] = decode_frame_4(level['walls_encoded'], 4096)

                monsters = []
                for i in range(30):
                    monster = Monster()
                    monster.type = reader.read_ubyte()
                    monster.unit = reader.read_ubyte()
                    monster.location = Location(reader)
                    monster.sub_position = reader.read_ubyte()
                    monster.direction = reader.read_ubyte()
                    monster.anim_step = reader.read_ubyte()
                    monster.frame = reader.read_ubyte()
                    monster.mode = reader.read_byte()
                    monster.f_9 = reader.read_byte()
                    monster.current_attack_frame = reader.read_ubyte()
                    monster.spell_status_left = reader.read_byte()
                    monster.hp_max = reader.read_short()
                    monster.hp_current = reader.read_short()
                    monster.dest = Location(reader)
                    monster.weapon = reader.read_ushort()
                    monster.pocket_item = reader.read_ushort()
                    monster.flags = reader.read_ubyte()
                    monster.idle_anim = reader.read_ubyte()
                    monster.remote_weapon = reader.read_byte()
                    monster.remote_attacks = reader.read_byte()
                    monster.palette = reader.read_byte()
                    monster.direction_changed = reader.read_byte()
                    monster.steps_until_remote_attack = reader.read_byte()
                    monster.pad_01 = reader.read_byte()

                    monsters.append(monster)
                level['monsters'] = monsters

                # Walls of force
                level['walls_of_force'] = []
                for i in range(5):
                    wof = {
                        "location": Location(reader),
                        "duration": reader.read_uint(),
                    }

                    level['walls_of_force'].append(wof)

                self.levels.append(level)

            # Game options
            assert reader.offset == 46792
            # reader.seek(46792)
            self.options = {
                "mouse_switch":  reader.read_byte(),
                "with_sounds":   reader.read_byte(),
                "bars_as_graph": reader.read_byte(),
            }

            # Special hand-spells which are special itemtypes [id from 51 to 57]
            # Offset: 46795
            assert reader.offset == 46795
            # reader.seek(46795)
            for i in range(51, 57):
                type = {
                    'slots':           str(ItemSlotFlags(reader.read_ushort())),
                    'flags':           str(ItemFlags(reader.read_ushort())),
                    'armor_class':     reader.read_byte(),
                    'allowed_classes': str(ProfessionFlags(reader.read_ubyte())),
                    'required_hand':   str(HandFlags(reader.read_ubyte())),
                    'damage_vs_small': str(Dice(reader)),
                    'damage_vs_big':   str(Dice(reader)),
                    'unknown':         reader.read_ubyte(),
                    'extra':           reader.read_ushort(),
                }
                assets['item_types'][i] = type

            c = self.champions[3]
            i = 1
