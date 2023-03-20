from tools.reader import BinaryReader

def vmp_decode():
    files = ['CRIMSON.VMP', 'DUNG.VMP', 'FOREST.VMP', 'MEZZ.VMP', 'SILVER.VMP']
    vmp = {}

    for file in files:

        with BinaryReader('data/{file}'.format(file=file)) as reader:
            count = reader.read_ushort()
            codes = reader.read_ushort(count)

        vmp[file] = {
            'count': count,
            'codes': codes,
        }

    return vmp


def vmp_draw(assets):
    files = ['CRIMSON', 'DUNG', 'FOREST', 'MEZZ', 'SILVER']

    for file in files:
        vcn = assets['vcn'][file + '.VCN']
        vmp = assets['vmp'][file + '.VMP']
        i = 1

