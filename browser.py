import os
import pickle

import numpy
from PIL import Image
from selenium import webdriver

from model import BoundingBox, Tile, Board


class Snapshot:
    def __init__(self, image=None):
        self._image: Image = image

        self.model = self.load_recognizer()

        os.makedirs('tiles-cache', exist_ok=True)

    @classmethod
    def load(cls, filename, box):
        with Image.open(filename) as image:
            image = image.crop(box.coordinates)
            image.save(filename)
        return cls(image)

    @staticmethod
    def load_recognizer():
        """Load pre-trained tile recognition model."""
        with open('tile_recognizer.pickle', 'rb') as fh:
            return pickle.load(fh)

    def datapoints_to_board(self):
        datapoints = self.extract_datapoints()
        value = self.model.predict(datapoints)
        return Board(numpy.resize(value, (4, 4)))

    def extract_datapoints(self):
        tile_offset = 101, 240
        tile_width, tile_height = 100, 148
        box = BoundingBox.from_dimensions(*tile_offset, tile_width, tile_height)
        x_pad, y_pad = 18, 10

        datapoints = []
        for i, j in [(i, j) for i in range(4) for j in range(4)]:
            x_offset = (box.width + x_pad) * j
            y_offset = (box.height + y_pad) * i
            tile_box = BoundingBox(box.left + x_offset,
                                   box.top + y_offset,
                                   box.right + x_offset,
                                   box.bottom + y_offset)
            tile = self._image.crop(tile_box.coordinates)
            tile = Tile(tile)
            datapoints.append(tile.to_datapoint())

        return datapoints

    def crop(self, box: BoundingBox):
        return self._image.crop(box.coordinates)


class Browser:

    def __init__(self, chrome_profile):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'user-data-dir={chrome_profile}')

        self._driver = webdriver.Chrome(options=chrome_options)

    def get(self, url):
        self._driver.get(url)

    def snapshot(self, filename):
        self._driver.save_screenshot(filename)
        window_size = self._driver.get_window_size()
        print(f"Captured snapshot")
        return window_size

    def close(self):
        self._driver.close()

