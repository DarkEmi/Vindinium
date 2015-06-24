__author__ = 'Emi'

class Game:
    size = 0
    tiles = None
    myStart = None
    taverns = None
    mines = None
    woods = None

    distances = None

    def __init__(self, json):
        print(type(json))
        board = json['game']['board']
        self.size = board['size']
        tiles = board['tiles']

        pos = 0
        self.tiles = [[0] * self.size] * self.size
        print(self.tiles)

        for i in range(self.size):
            for j in range(self.size):
                tile = tiles[pos:pos + 2]
                pos += 2
                if tile == '##':
                    tile = 'wood'
                elif tile == '  ':
                    tile = ''
                elif tile == '[]':
                    tile = 'tavern'
                elif tile[0] == '@':
                    tile = 'p' + tile[1]
                elif tile[0] == '$':
                    tile = 'm' + tile[1]

                self.tiles[i][j] = Tile(i, j, txt)

        print(self.tiles)

    def findpaths(self, origin):
        self.distances = [[-1] * self.size ] * self.size




class Tile:
    x, y = 0
    dist = -1
    ownedby = -1
    text = None

    def Tile(self, x, y):
        self.x = x
        self.y = y
