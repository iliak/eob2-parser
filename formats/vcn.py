import os
import struct

from decoders import format80_decode
from tools.reader import BinaryReader


def vcn_decode():
    files = ['CRIMSON.VCN', 'DUNG.VCN', 'FOREST.VCN', 'MEZZ.VCN', 'SILVER.VCN']
    vcn = {}

    input_path = './data/'
    output_path = './build/decoded/'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in files:
        vcn[filename] = {}


        # Decode file
        data = format80_decode(f'{input_path}/{filename}')

        # Save uncompressed file
        target = f"{output_path}{filename}.uncps"
        with open(target, "wb") as handle:
            s = struct.pack('{count}B'.format(count=len(data)), *data)
            handle.write(s)

        # Process file
        with BinaryReader(target) as reader:

            # Export content
            vcn[filename]['count'] = reader.read_ushort()
            vcn[filename]['palette_backdrop'] = reader.read_ubyte(16)
            vcn[filename]['palette_wall'] = reader.read_ubyte(16)
            shapes = []
            for i in range(vcn[filename]['count']):
                raw = reader.read_byte(32)
                shapes.append(raw)
            vcn[filename]['shapes'] = shapes


            # Draw the file


    return vcn
