from PIL import Image, ImageDraw


def decorations_generate(assets):
    path = "build/"
    for name in assets['decorations']:
        decoration = assets['decorations'][name]
        img = Image.new('RGB', (320, 200))

        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, 640, 480], 'white')
        for rect in decoration['rectangles']:
            x = rect[0]
            y = rect[1]
            right = x + rect[2]
            bottom = y + rect[3]
            d.rectangle([x, y, right, bottom], 'blue', 'red')

        img.resize((640, 400))
        img.save('{path}{name}.png'.format(path=path, name=name))


def gen_crimson(assets):
    deco = assets['decorations']['CRIMSON.DEC']
    cps = Image.open('data/CRIMSON.PNG')

    img = Image.new('RGB', (320, 200))

    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 640, 480], 'white')

    for rect in deco['rectangles']:
        x = rect[0]
        y = rect[1]
        right = x + rect[2]
        bottom = y + rect[3]

        region = cps.crop([x, y, right, bottom])
        img.paste(region, box=[x, y])

        img.save('build/CRIMSON_decoded.PNG')

        i = 1


def decorations_dump(decs):
    sprites = {}
    decorations = {}
    for slug in decs:
        dec = decs[slug]

        sprites[slug] = {}
        for key, shape in enumerate(dec["shapes"]):
            sprites[slug][f"{key}"] = {
                "x":        shape[0] * 2,
                "y":        shape[1] * 2,
                "width":    shape[2] * 2,
                "height":   shape[3] * 2,
                "x_offset": 0,
                "y_offset": 0,
            }

        decorations[slug] = {}
        for key, shape in enumerate(dec["decorations"]):
            positions = [
                ['t'],  # 0
                ['l'],  # 1
                ['h'],  # 2
                ['c'],  # 3
                ['n', 'o'],  # 4
                ['k', 'm'],  # 5
                ['g', 'i'],  # 6
                ['b', 'd'],  # 7
                ['f', 'j'],  # 8
                ['a', 'e'],  # 9
            ]

            decorations[slug][f"{key}"] = {
                "forcedisplay": False,
                "isblocking":   False,
                "hideitems":    False,
                "onhack":       None,
                "onbash":       None,
                "onclick":      None,
                "item":         {
                    "x": 0,
                    "y": 0
                },
            }
            for id, pos in enumerate(positions):
                frame = {
                    "x":     0,
                    "y":     0,
                    "flip":  "",
                    "frame": "",
                }

                frame_id = shape['shapes'][id]
                if frame_id != -1:
                    frame["frame"] = f'{frame_id}'
                    frame["x"] = shape["shape_x"][id] * 2
                    frame["y"] = shape["shape_y"][id] * 2

                for p in pos:
                    decorations[slug][f"{key}"][p] = frame

            i = 1
    # dump("sprites.json", sprites)
    # dump("decorations.json", decorations)
