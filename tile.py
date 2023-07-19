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

    def merge(self, other):
        is_1_2 = (self.value, other.get_value()) in [(1, 2), (2, 1)]
        is_3ish = (self.value == other.get_value() and self.value >= 3)
        if other and (is_1_2 or is_3ish):
            self.value = 3 if self.value in [1, 2] else self.value * 2
            return True
        return False
