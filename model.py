import numpy
from PIL import Image


class Box:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.bottom - self.top

    @property
    def coordinates(self):
        return self.left, self.top, self.right, self.bottom

    @classmethod
    def from_dimensions(cls, left, top, width, height):
        return cls(left, top, left + width, top + height)


class Tile:

    def __init__(self, image: Image):
        self.image = image

    def to_datapoint(self, resolution=20):
        dimensions = (resolution, round(resolution * 1.5))
        tile = self.image.convert(mode='L').resize(dimensions)
        return numpy.asarray(tile).flatten()