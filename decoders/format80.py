def format80_decode(reader):
    size = reader.read_ushort()
    type = reader.read_ushort()
    uncompressed = reader.read_uint()
    palette = reader.read_ushort()

    if type != 0x4:
        raise TypeError

    data = [None] * uncompressed
    dst_offset = 0
    while True:
        code = reader.read_ubyte()

        # end code
        if code == 0x80:
            return data

        # 0b10######
        elif code & 0xC0 == 0x80:
            count = code & 0x3f
            for i in range(count):
                data[dst_offset] = reader.read_ubyte()
                dst_offset += 1

        # 0b11######
        elif code & 0xC0 == 0xC0:
            count = code & 0x3f

            # Large copy
            if count < 0x3E:
                count += 3
                offset = reader.read_ushort()
                for i in range(offset, offset + count):
                    data[dst_offset] = data[i]
                    dst_offset += 1

            # Very large copy
            elif count == 0x3F:
                pass

            else:
                i = 1

        # 0b0#######
        elif code & 0x80 == 0:
            count = ((code & 0x70) >> 4) + 3
            offset = reader.read_ubyte() + ((code & 0x0F) << 8)
            offset = dst_offset - offset
            for i in range(offset, offset + count):
                data[dst_offset] = data[i]
                dst_offset += 1

        else:
            i = 1
