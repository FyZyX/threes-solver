class Tile:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.value == other.value  # or whatever attributes you have in Tile class

    def get_value(self):
        return self.value

    def merge(self, other):
        if other and ((self.value, other.get_value()) in [(1, 2), (2, 1)] or (self.value == other.get_value() and self.value >= 3)):
            self.value = 3 if self.value in [1, 2] else self.value * 2
            return True
        return False
