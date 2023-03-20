import struct

from decoders import format80_decode
from tools.reader import BinaryReader


def vcn_decode():
    files = ['CRIMSON.VCN', 'DUNG.VCN', 'FOREST.VCN', 'MEZZ.VCN', 'SILVER.VCN']
    vcn = {}

    for file in files:
        vcn[file] = {}

        with BinaryReader('data/{file}'.format(file=file)) as reader:
            data = format80_decode(reader)

            with open("data/{file}.uncps".format(file=file), "wb") as handle:
                s = struct.pack('{count}B'.format(count=len(data)), *data)
                handle.write(s)

            # continue
        with BinaryReader('data/{file}.uncps'.format(file=file)) as reader:

            vcn[file]['count'] = reader.read_ushort()
            vcn[file]['palette_backdrop'] = reader.read_ubyte(16)
            vcn[file]['palette_wall'] = reader.read_ubyte(16)
            shapes = []
            for i in range(vcn[file]['count']):
                raw = reader.read_byte(32)
                shapes.append(raw)
            vcn[file]['shapes'] = shapes
            i = 1

    return vcn
