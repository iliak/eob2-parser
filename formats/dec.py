from tools.reader import BinaryReader


def dec_decode():
    # .DEC

    files = ['AZURE.DEC', 'BROWN.DEC', 'CRIMSON.DEC', 'FOREST.DEC', 'MEZZ.DEC', 'SILVER.DEC']
    decorations = {}

    for file in files:
        decorations[file] = {
            'decorations': [],
            'shapes': [],
        }
        with BinaryReader('data/{file}'.format(file=file)) as reader:
            count = reader.read_ushort()

            for i in range(count):
                deco = {
                    'shapes':  [-1 if value == 255 else value for value in reader.read_ubyte(10)],
                    'next':    reader.read_byte(),
                    'flags':   reader.read_byte(),          # horizontal/vertical flip ?
                    'shape_x': reader.read_short(10),
                    'shape_y': reader.read_short(10),
                }
                decorations[file]['decorations'].append(deco)

            count = reader.read_ushort()
            for i in range(count):
                rect = list(reader.read_ushort(4))
                rect[0] *= 8
                rect[2] *= 8
                decorations[file]['shapes'].append(rect)

    return decorations



def dec_draw(assets):
    files = ['AZURE', 'BROWN', 'CRIMSON', 'FOREST', 'MEZZ', 'SILVER']

    for file in files:
        dec = assets['dec'][file + '.DEC']
        i = 1

