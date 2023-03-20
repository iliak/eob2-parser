from tools.reader import BinaryReader


def item_decode(assets):
    items = []  # ITEM.DAT
    with BinaryReader('data/ITEM.DAT') as reader:
        count = reader.read_ushort()
        for i in range(count):
            item = {
                'unidentified_name': reader.read_ubyte(),
                'identified_name':   reader.read_ubyte(),
                'flags':             reader.read_ubyte(),
                'picture':           reader.read_ubyte(),
                'type':              reader.read_ubyte(),  # See types below

                # Where the item lies at position
                # In Maze:
                #      0..3-> Bottom
                #      4..7-> Wall (N,E,S,W)
                # For EotB I: 0..3-> Floor NW,NE,SW,SE
                #                8-> Compartment
                # If in inventory:
                #      0..26-> Position in Inventory
                'sub_position':      reader.read_ubyte(),

                # Position in maze x + y * 32 | 0 => Consumed
                'coordinate':        reader.read_ushort(),
                'next':              reader.read_ushort(),
                'previous':          reader.read_ushort(),

                # Level, where the item lies, 0 <= no level
                'level':             reader.read_ubyte(),

                # The value of item, -1 if consumed
                'value':             reader.read_byte(),
            }
            pos = divmod(item['coordinate'], 32)
            item['coordinate'] = {'x': pos[1], 'y': pos[0]}
            items.append(item)

        count = reader.read_ushort()
        for i in range(count):
            name = reader.read_string(35)
            assets['item_names'].append(name)

        for item in items:
            item['unidentified_name'] = assets['item_names'][item['unidentified_name']]
            item['identified_name'] = assets['item_names'][item['identified_name']]

    return items
