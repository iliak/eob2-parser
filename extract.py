#!/usr/bin/env python3.10

import json
import os

from commons import ItemFlags
from formats.dcr import dcr_decode
from formats.dec import dec_decode
from formats.inf import inf_decode
from formats.item import item_decode
from formats.itemtypes import itemtypes_decode
from formats.maz import maz_decode
from formats.pal import pal_decode
from formats.text import text_decode
from formats.vcn import vcn_decode
from formats.vmp import vmp_decode

assets = {
    "items":       [],
    "item_types":  [],
    "item_names":  [],
    'texts':       [],
    'level_items': [],
    'inf':         {},
    'maz':         {},
    'pal':         {},
    'vmp':         {},
    'vcn':         {},
    'dec':         {}
}


def dump():
    path = './build'
    if not os.path.exists(path):
        os.makedirs(path)

    for name in assets:
        with open('{path}/{name}.json'.format(path=path, name=name), 'w') as handle:

            if name == 'maz':
                data = []
            elif name == 'inf':
                data = [assets['inf'][i].decode(assets) for i in assets['inf']]
            else:
                data = assets[name]

            json.dump(data, handle, indent=True, sort_keys=True)


# http://www.shikadi.net/moddingwiki/Eye_of_the_Beholder
if __name__ == '__main__':
    # PAL: color palettes
    assets['pal'] = pal_decode()

    # DEC: decoration rectangle
    assets['dec'] = dec_decode()

    # VMP: information about how to put together the blocks defined in the corresponding vcn files, into proper walls
    assets['vmp'] = vmp_decode()

    # VCN: graphics for the walls including the background
    assets['vcn'] = vcn_decode()

    # DCR: monster graphics
    assets['dcr'] = dcr_decode()

    # TEXT.DAT
    assets['texts'] = text_decode()

    # ITEMTYPE.DAT
    assets['item_types'] = itemtypes_decode()

    # ITEM.DAT
    assets['items'] = item_decode(assets)

    # Rebuild items in levels
    level_items = [{
        'flags':      str(ItemFlags(item['flags'])),
        'type':       assets['item_types'][item['type']],
        'picture':    item['picture'],
        'value':      item['value'],
        'coordinate': {
            'level': item['level'],
            'x':     item['coordinate']['x'],
            'y':     item['coordinate']['y'],
        }
    } for item in assets['items']]

    # MAZ:  Maps
    assets['maz'] = maz_decode()

    # INF: Maps
    assets['inf'] = inf_decode()

    dump()
    exit()

    # Savegame
    savegame = Savegame('data/EOBDATA2.SAV')

    dcr_draw(assets)
    vmp_draw(assets)
    dec_draw(assets)

    decorations_dump(assets["dec"])

    gen_crimson()
