import numpy
from PIL import Image


class BoundingBox:

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


class Board:
    def __init__(self, tiles=None, dimension=4):
        self._dimension = dimension
        self.tiles = tiles if tiles is not None else numpy.zeros((4, 4))

    def from_datapoints(self, image: Image):
        datapoints = self.extract_datapoints(image)
        value = self.model.predict(datapoints)
        return Board(numpy.resize(value, (4, 4)))

    def set_tile(self, i, j, tile):
        self.tiles[i, j] = tile
