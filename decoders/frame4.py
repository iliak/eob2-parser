def frame4_decode(data, size):
    dst = [None] * size
    offset_src = 0
    offset_dst = 0

    while True:
        count = size - offset_dst
        if count == 0:
            break

        code = data[offset_src]
        offset_src += 1
        if (code & 0x80) != 0x80:
            length = min(count, (code >> 4) + 3)
            offs = ((code & 0xF) << 8)

        elif (code & 0x40) == 0x40:
            i = 2
        elif code != 0x80:
            length = min(count, code & 0x3F)
            for i in range(length):
                dst[offset_src + i] = data[offset_dst + i]
            offset_src += length
            offset_dst += length
