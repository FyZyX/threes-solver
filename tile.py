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

    def set_value(self, value):
        self.value = value

    def can_merge_with(self, other):
        if not other:
            return False

        if (self.value, other.get_value()) in [(1, 2), (2, 1)]:
            return True
        if self.value == other.get_value() and self.value >= 3:
            return True

        return False

    def merge(self, other):
        if self.can_merge_with(other):
            if self.value in [1, 2]:
                self.value = 3
            else:
                self.value *= 2
