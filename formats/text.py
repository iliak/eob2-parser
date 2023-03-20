import os

from tools.reader import BinaryReader


def text_decode():
    file = 'data/TEXT.DAT'
    offsets = []
    msg = []
    with BinaryReader(file) as reader:
        while True:
            offset = reader.read_ushort()
            offsets.append(offset)
            if reader.offset >= offsets[0]:
                break

        for id, offset in enumerate(offsets):

            if id == len(offsets) - 1:
                length = os.path.getsize(file) - offsets[id]
            else:
                length = offsets[id + 1] - offsets[id]

            msg.append(reader.read_string(length))

    return msg
