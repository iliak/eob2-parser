from tools.reader import BinaryReader


class Maz:
    """

    """

    def __init__(self):

        self.width = None
        self.height = None
        self.faces = None
        self.walls = []

    def process(self, filename):
        with BinaryReader('data/{file}.MAZ'.format(file=filename)) as reader:

            self.width = reader.read_ushort()
            self.height = reader.read_ushort()
            self.faces = reader.read_ushort()

            self.walls = [[None for y in range(self.height)] for x in range(self.width)]

            for y in range(self.height):
                for x in range(self.width):
                    n = reader.read_ubyte()
                    s = reader.read_ubyte()
                    w = reader.read_ubyte()
                    e = reader.read_ubyte()

                    self.walls[x][y] = {
                        'n': n,
                        's': s,
                        'w': w,
                        'e': e,
                    }

    def _decode(self):

        blocks = [['#' for y in range(self.height)] for x in range(self.width)]

        for y in range(self.height):
            for x in range(self.width):
                block = self.walls[y][x]

                if block['n'] == 0 and block['e'] == 0 and block['s'] == 0 and block['w'] == 0:
                    blocks[y][x] = " "

                # if block['n'] in (1, 2):
                #     blocks[y][x] = "#"
                #
                # if block['s'] in (1, 2) and y < self.height -1:
                #     blocks[y][x] = "#"
                #
                # if block['w'] in (1, 2):
                #     blocks[y][x] = "#"
                #
                # if block['e'] in (1, 2) and x < self.width -1:
                #     blocks[y][x] = "#"

                # if block['n'] == 0 and block['e'] == 0 and block['s'] == 0 and block['w'] == 0:
                #     wall = ' '
                # else:
                #     wall = '#'
                #
                # blocks[y][x] = wall

        return [''.join(row) for row in blocks]





def maz_decode():
    # Read wall decorations
    files = [
        'LEVEL1',
        'LEVEL2',
        'LEVEL3',
        'LEVEL4',
        'LEVEL5',
        'LEVEL6',
        'LEVEL7',
        'LEVEL8',
        'LEVEL9',
        'LEVEL10',
        'LEVEL11',
        'LEVEL12',
        'LEVEL13',
        'LEVEL14',
        'LEVEL15',
    ]
    mazes = {}
    for file in files:
        maze = Maz()
        maze.process(file)
        mazes[file] = maze

    return mazes

