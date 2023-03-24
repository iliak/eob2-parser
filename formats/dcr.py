import os

from PIL import Image

from tools.reader import BinaryReader


def dcr_decode():
    files = ['BEHOLDER.DCR', 'CLERIC1.DCR', 'CLERIC2.DCR', 'CLERIC3.DCR', 'DRAGON.DCR', 'GUARD1.DCR', 'GUARD2.DCR', 'MAGE.DCR', 'MANTIS.DCR']
    dcr = {}

    for file in files:
        dcr[file] = []
        with BinaryReader(f'data/{file}') as reader:
            count = reader.read_ushort()
            for i in range(count):
                sides = []
                for j in range(6):
                    side = {
                        "cps_x":    reader.read_ubyte() * 8,
                        "cps_y":    reader.read_ubyte(),
                        "width":    reader.read_ubyte() * 8,
                        "height":   reader.read_ubyte(),
                        "screen_x": reader.read_ubyte(),
                        "screen_y": reader.read_ubyte()
                    }

                    sides.append(side)
                dcr[file].append(sides)

            i = 1
    return dcr


def dcr_draw(assets):
    files = ['BEHOLDER', 'CLERIC1', 'CLERIC2', 'CLERIC3', 'DRAGON', 'GUARD1', 'GUARD2', 'MAGE', 'MANTIS']
    input_path = './data/'
    output_path = './build/dcr/'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for file in files:
        dcr = assets['dcr'][file + '.DCR']

        for id in range(len(dcr)):
            data = dcr[id]
            img = Image.open("{path}{file}.PNG".format(path=input_path, file=file), 'r')
            # img.convert('RGBA')

            for face in range(6):
                d = data[face]

                x = d['cps_x']
                y = d['cps_y']
                right = x + d['width']
                lower = y + d['height']

                bg = Image.new('RGBA', (320, 200), (255, 0, 0, 0))
                bg.paste(img, (0, 0))

                crop = bg.crop((x, y, right, lower))
                # crop.convert('RGBA')

                x = d['screen_x']
                y = d['screen_y']
                bg.paste(crop, (x, y), )

                bg = bg.resize((640, 400))
                bg.save("{path}{file}_{id}_{face}.PNG".format(path=output_path, file=file, id=id, face=face), format='png')

            i = 1
