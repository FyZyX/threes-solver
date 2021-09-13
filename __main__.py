import os
import time

from browser import Snapshot
from model import BoundingBox

USER = os.environ.get('USER', 'lucaslofaro')
CHROME_PROFILE = os.path.join(os.sep, 'Users', USER, '.config', 'google-chrome')
SNAPSHOT_FILE = 'snapshot.png'


def save_training_image(image, coords):
    tile = image.convert(mode='L').resize((20, round(20 * 1.5)))
    i, j = coords
    tile.save(f'tiles-cache/tile-{i}-{j}-train-{int(time.time())}.png')



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
