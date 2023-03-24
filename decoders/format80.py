from tools.reader import BinaryReader


def format80_decode(filename):
    with BinaryReader(filename) as reader:
        size = reader.read_ushort()
        length = reader.get_size()

        if size + 2 != length:
            print(f"{filename}: length warning: stored={size}, actual={length}")
            return

        type = reader.read_ushort()
        if type != 4:
            print(f"{filename}: not Format80 compressed")
            return

        uncompressed = reader.read_uint()
        palette = reader.read_ushort()

        data = [0] * uncompressed
        offset = 0
        while True:
            code = reader.read_ubyte()

            if code == 0xFE:
                len = code & 0x38 + 3  # Get the count from the first 6bits of the code
                for i in range(len):
                    data[offset] = reader.read_ubyte()
                    offset += 1
            else:

                # 0b11###### Copy count bytes from pos to absolute dest
                if code >= 0xC0:
                    if code == 0xFF:
                        len = reader.read_ushort()
                    else:
                        len = (code & 0x3F) + 3

                    offset = reader.read_ushort()

                # end code
                elif code == 0x80:
                    return data

                elif code > 0x80:
                    len = code & 0x3f

                else:
                    # TODO
                    pass

                # while len > 0:
                for i in range(len):
                    data[offset] = reader.read_ubyte()
                    offset += 1
                    # len -= 1
