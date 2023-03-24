import os
import struct

from decoders import format80_decode
from tools.reader import BinaryReader


def cps_decode():
    files = [
        'AIRSEAL.CPS', 'ALTAR.CPS', 'ANT.CPS', 'ASERVANT.CPS', 'AZURE1.CPS', 'AZURE2.CPS', 'BADMOOD.CPS', 'BASILISK.CPS', 'BEHOLDER.CPS', 'BLOOD.CPS', 'BORDER.CPS', 'BROWN1.CPS',
        'BROWN2.CPS', 'BROWN3.CPS', 'BULETTE.CPS', 'CHARGENA.CPS', 'CHARGENB.CPS', 'CHARGEN.CPS', 'CHOICE.CPS', 'CLERIC1.CPS', 'CLERIC2.CPS', 'CLERIC3.CPS', 'COIN.CPS', 'CREDITS2.CPS',
        'CREDITS3.CPS', 'CREDITS.CPS', 'CRIMRING.CPS', 'CRIMSON2.CPS', 'CRIMSON.CPS', 'CRYSTAL.CPS', 'CUBE.CPS', 'DARKMOON.CPS', 'DECORATE.CPS', 'DESTROY0.CPS', 'DESTROY1.CPS',
        'DESTROY2.CPS', 'DESTROY3.CPS', 'DOOR1.CPS', 'DOOR2.CPS', 'DOORWAY1.CPS', 'DOORWAY2.CPS', 'DRAGON1.CPS', 'DRAGON2.CPS', 'DRAGON.CPS', 'DRANAZ3.CPS', 'DRAN.CPS', 'DRANSL2.CPS',
        'DRANX.CPS', 'DREAM.CPS', 'FOREST.CPS', 'FRGIANT.CPS', 'FSNAKE.CPS', 'GARGOYLE.CPS', 'GASSPORE.CPS', 'GLASS.CPS', 'GUARD1.CPS', 'GUARD2.CPS', 'GUARDIAN.CPS', 'HEAD.CPS',
        'HELLHND.CPS', 'HEROES.CPS', 'HURRY1.CPS', 'HURRY2.CPS', 'IMPLODE.CPS', 'INTRO.CPS', 'INVENT.CPS', 'ITEMICN.CPS', 'ITEML1.CPS', 'ITEMS1.CPS', 'KHELBAN1.CPS', 'KHELBAN2.CPS',
        'KHELBAN3.CPS', 'KHELBAN4.CPS', 'KHELBAN5.CPS', 'KHELBAN6.CPS', 'KHELBEN.CPS', 'KHELDRAN.CPS', 'MAGE.CPS', 'MAGIC.CPS', 'MANTIS.CPS', 'MAP.CPS', 'MEDUSA.CPS', 'MENU.CPS',
        'MEZZ1.CPS', 'MEZZ2.CPS', 'MINDFLAY.CPS', 'MMOUTH1.CPS', 'MMOUTH2.CPS', 'OUTPORTS.CPS', 'OUTTAKE.CPS', 'PLAYFLD.CPS', 'PORTALA.CPS', 'PORTALB.CPS', 'SALAMNDR.CPS', 'SHRUNKEN.CPS',
        'SILVER1.CPS', 'SILVER2.CPS', 'SKELWAR.CPS', 'SOUT1.CPS', 'SOUT2.CPS', 'SOUT3.CPS', 'SOUT4.CPS', 'SOUT5.CPS', 'SPIDER.CPS', 'STONEGIA.CPS', 'STREET1.CPS', 'STREET2.CPS',
        'SUICIDE.CPS', 'TANGLOR.CPS', 'THANKS.CPS', 'THROWN.CPS', 'WASP.CPS', 'WESTWOOD.CPS', 'WILLOWIS.CPS', 'WINDING.CPS', 'WOLF.CPS',
    ]
    input_path = './data/'
    output_path = './build/decoded/'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cps = {}

    for file in files:
        cps[file] = []
        print(f"[CPS]: {file}")

        # Decode file
        data = format80_decode(f"{input_path}{file}")

        # Save uncompressed file
        target = f"{output_path}{file}.uncps"
        with open(target, "wb") as handle:
            s = struct.pack(f'{len(data)}B', *data)
            handle.write(s)

        # Process file
        with BinaryReader(target) as reader:
            count = reader.read_ushort()
            # for i in range(count):
            #     sides = []
            #     for j in range(6):
            #         side = {
            #             "cps_x":    reader.read_ubyte() * 8,
            #             "cps_y":    reader.read_ubyte(),
            #             "width":    reader.read_ubyte() * 8,
            #             "height":   reader.read_ubyte(),
            #             "screen_x": reader.read_ubyte(),
            #             "screen_y": reader.read_ubyte()
            #         }
            #
            #         sides.append(side)
            #     dcr[file].append(sides)

            i = 1
    return cps
