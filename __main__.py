import os
import time
from collections import namedtuple

from PIL import Image
from selenium import webdriver

USER = os.environ.get('USER', 'lucaslofaro')

Dimensions = namedtuple('Dimension', ('x_offset', 'y_offset', 'width', 'height'))


def chrome_profile_path(user):
    return os.path.join(os.sep, 'Users', user, '.config', 'google-chrome')


class Snapshot:
    def __init__(self, filename, size):
        self.filename = filename

        game_width, game_height = 654, 976
        game_x_offset = 8  # No idea why I have to do this...
        game_y_offset = 32
        # This is pretty counter-intuitive...feels like I should taking half the
        # remaining width (browser width - game width), but this works I guess
        width = size['width'] - game_width / 2 - game_x_offset
        dim = Dimensions(width, game_y_offset, game_width, game_height)
        self.crop(dim)

        os.makedirs('tiles', exist_ok=True)

    @staticmethod
    def crop_tiles(board):
        # Upper-left corner of first tile
        dim = Dimensions(101, 240, 100, 148)
        x_pad, y_pad = 18, 10

        left, top = dim.x_offset, dim.y_offset
        right, bottom = left + dim.width, top + dim.height
        for i in range(4):
            for j in range(4):
                x_offset = (dim.width + x_pad) * j
                y_offset = (dim.height + y_pad) * i
                tile = board.crop((left + x_offset, top + y_offset,
                                   right + x_offset, bottom + y_offset))
                tile.save(f'tiles/tile-{i}-{j}.png')

    def crop(self, dim):
        board = Image.open(self.filename)

        left, top = dim.x_offset, dim.y_offset
        right, bottom = left + dim.width, top + dim.height
        board = board.crop((left, top, right, bottom))

        self.crop_tiles(board)
        board.save(self.filename)


class Browser:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        options = {
            'user-data-dir': chrome_profile_path(USER),
        }
        [chrome_options.add_argument(f'{option}={value}')
         for option, value in options.items()]

        self._browser = webdriver.Chrome(options=chrome_options)

    def get(self, url):
        self._browser.get(url)

    def snapshot(self, outfile):
        self._browser.save_screenshot(outfile)
        window_size = self._browser.get_window_size()
        snap = Snapshot(outfile, window_size)
        print(f"Captured snapshot: '{outfile}'")
        return snap


class Game:
    url = 'http://play.threesgame.com/'

    def __init__(self):
        self.browser = Browser()

        self.open()

    def open(self, load_wait=2):
        print(f'Opening {self.url} ...')
        self.browser.get(self.url)

        # Capture initial board position
        print(f'Allowing {load_wait} seconds for game to load ...')
        time.sleep(load_wait)
        self.browser.snapshot('snapshot.png')


if __name__ == '__main__':
    Game()
