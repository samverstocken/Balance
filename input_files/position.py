class position(self, x, y):
    self.x = x
    self.y = y

    def distance(self, pos):
        return abs(pos.x - self.x) + abs(pos.y - self.y)
