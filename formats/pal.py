from tools.reader import BinaryReader


def pal_decode():
    files = ['AZURE.PAL', 'CRIMSON.PAL', 'DUNG.PAL', 'FINALE_0.PAL', 'FINALE_1.PAL', 'FINALE_2.PAL', 'FINALE_3.PAL',
             'FINALE_4.PAL', 'FINALE_5.PAL', 'FINALE_6.PAL', 'FINALE_7.PAL', 'FOREST.PAL', 'MEZZ.PAL', 'PALETTE0.PAL',
             'PALETTE1.PAL', 'PALETTE2.PAL', 'PALETTE3.PAL', 'PALETTE4.PAL', 'SILVER.PAL']
    pal = {}

    for file in files:
        colors = []

        with BinaryReader('data/{file}'.format(file=file)) as reader:
            for i in range(256):
                r = reader.read_byte()
                g = reader.read_byte()
                b = reader.read_byte()

                colors.append({
                    "r": r,
                    "g": g,
                    "b": b,
                })

        pal[file] = colors

    return pal
