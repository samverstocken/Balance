class Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pos):
        return abs(pos.x - self.x) + abs(pos.y - self.y)

    def __eq__(self, pos):
        return self.x == pos.x and self.y == pos.y

    def moveleft(self):
        self.x -= 1

    def moveright(self):
        self.x += 1

    def moveup(self):
        self.y += 1

    def movedown(self):
        self.y -= 1
