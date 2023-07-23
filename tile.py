class Tile:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.value == other.value

    def get_value(self):
        return self.value

    def can_merge(self, tile: "Tile"):
        is_1_2 = (self.value, tile.get_value()) in [(1, 2), (2, 1)]
        if is_1_2:
            return True

        is_3ish = (self.value == tile.get_value() and self.value >= 3)
        if is_3ish:
            return True

        return False

    def merge(self, tile: "Tile"):
        if tile and self.can_merge(tile):
            self.value += tile.get_value()
            return True
        return False
