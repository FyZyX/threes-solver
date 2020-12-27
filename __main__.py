import os
import pickle
import time

import numpy
from PIL import Image
from selenium import webdriver

from model import BoundingBox, Tile, Board

USER = os.environ.get('USER', 'lucaslofaro')
CHROME_PROFILE = os.path.join(os.sep, 'Users', USER, '.config', 'google-chrome')
SNAPSHOT_FILE = 'snapshot.png'


def save_training_image(image, coords):
    tile = image.convert(mode='L').resize((20, round(20 * 1.5)))
    i, j = coords
    tile.save(f'tiles-cache/tile-{i}-{j}-train-{int(time.time())}.png')


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
    options = {
        'user-data-dir': CHROME_PROFILE,
    }

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        for option, value in self.options.items():
            chrome_options.add_argument(f'{option}={value}')

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


class Game:
    url = 'http://play.threesgame.com/'

    def __init__(self):
        self.board = None
        self.browser = Browser()

    def start(self, load_wait=2):
        print(f'Opening {self.url} ...')
        self.browser.get(self.url)

        print(f'Allowing {load_wait} seconds for game to load ...')
        time.sleep(load_wait)

    def play(self):
        self.start()
        while True:
            self.parse()
            whatiwant = input('What you want? ')
            if whatiwant == 'exit':
                self.browser.close()
                whatiwant = 'done'
            if whatiwant in 'done':
                break
            print('AHHHHHH!', whatiwant)

    def get_next_move_box(self):
        return BoundingBox.from_dimensions(302, 83, 50, 69)

    def get_board_box(self, size):
        # TODO: Move magic numbers to more appropriate place
        board_width, board_height = 654, 976
        board_x_offset = 8  # No idea why I have to do this...
        board_y_offset = 32
        # This is pretty counter-intuitive...feels like I should taking half the
        # remaining width (browser width - game width), but this works I guess
        width = size['width'] - board_width / 2 - board_x_offset
        return BoundingBox.from_dimensions(
            width, board_y_offset, board_width, board_height)

    def parse(self):
        # Capture board position
        window_size = self.browser.snapshot(SNAPSHOT_FILE)
        box = self.get_board_box(window_size)
        snap = Snapshot.load(SNAPSHOT_FILE, box)
        box = self.get_next_move_box()
        snap.crop(box).show()
        self.board = snap.datapoints_to_board()
        print(self.board.tiles)


if __name__ == '__main__':
    Game().play()
