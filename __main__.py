import os
import pickle
import time

import numpy
from PIL import Image
from selenium import webdriver

from model import Box, Tile

USER = os.environ.get('USER', 'lucaslofaro')
CHROME_PROFILE = os.path.join(os.sep, 'Users', USER, '.config', 'google-chrome')
SNAPSHOT_FILE = 'snapshot.png'


def save_training_image(image, coords):
    tile = image.convert(mode='L').resize((20, round(20 * 1.5)))
    i, j = coords
    tile.save(f'tiles-cache/tile-{i}-{j}-train-{int(time.time())}.png')


class Snapshot:
    def __init__(self, size):
        self.filename = SNAPSHOT_FILE

        self.model = self.load_recognizer()

        game_width, game_height = 654, 976
        game_x_offset = 8  # No idea why I have to do this...
        game_y_offset = 32
        # This is pretty counter-intuitive...feels like I should taking half the
        # remaining width (browser width - game width), but this works I guess
        width = size['width'] - game_width / 2 - game_x_offset
        box = Box.from_dimensions(width, game_y_offset, game_width, game_height)
        self.crop(box)

        os.makedirs('tiles-cache', exist_ok=True)

    @staticmethod
    def load_recognizer():
        """Load pre-trained tile recognition model."""
        with open('tile_recognizer.pickle', 'rb') as fh:
            return pickle.load(fh)

    def crop_tiles(self, board: Image):
        box = Box.from_dimensions(101, 240, 100, 148)
        x_pad, y_pad = 18, 10

        tiles = []
        for i, j in [(i, j) for i in range(4) for j in range(4)]:
            x_offset = (box.width + x_pad) * j
            y_offset = (box.height + y_pad) * i
            tile_box = Box(box.left + x_offset,
                           box.top + y_offset,
                           box.right + x_offset,
                           box.bottom + y_offset)
            tile = board.crop(tile_box.coordinates)
            tile = Tile(tile)
            tiles.append(tile.to_datapoint())
            # save_training_image(tile, (i, j))

        value = self.model.predict(tiles)
        board = numpy.resize(value, (4, 4))
        print(board)

    def crop(self, box):
        with Image.open(self.filename) as board:
            board = board.crop(box.coordinates)

            self.crop_tiles(board)
            board.save(self.filename)


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

    def snapshot(self):
        self._driver.save_screenshot(SNAPSHOT_FILE)
        window_size = self._driver.get_window_size()
        snap = Snapshot(window_size)
        print(f"Captured snapshot")
        return snap


class Game:
    url = 'http://play.threesgame.com/'

    def __init__(self):
        self.board = None
        self.browser = Browser()
        self.start()

    def start(self, load_wait=2):
        print(f'Opening {self.url} ...')
        self.browser.get(self.url)

        print(f'Allowing {load_wait} seconds for game to load ...')
        time.sleep(load_wait)

    def play(self):
        while True:
            self.parse_board()
            whatiwant = input('What you want? ')
            print('AHHHHHH!', whatiwant)

    def parse_board(self):
        # Capture board position
        self.board = self.browser.snapshot()


if __name__ == '__main__':
    g = Game()
    g.play()
