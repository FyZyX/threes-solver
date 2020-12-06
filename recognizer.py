import os
import pickle

import numpy
from PIL import Image
from sklearn import svm

from model import Tile


class TileRecognizer:
    def __init__(self):
        self.classifier = svm.SVC(gamma=0.001, C=100)

    def load_tiles(self):
        # TODO: This should really pull from a well defined training data location
        tiles, labels = [], []
        for file in os.listdir('tiles-labelled'):
            with Image.open(f'tiles-labelled/{file}') as image:
                tile = Tile(image)
                tiles.append(tile.to_datapoint())
                label = int(file.split('-')[1].split('.')[0])
                labels.append(label)
        return numpy.array(tiles), labels

    def train_model(self, data, labels):
        # TODO: Possibly read training data from object
        self.classifier.fit(data, labels)

    def persist_model(self):
        with open('tile_recognizer.pickle', 'wb') as fh:
            pickle.dump(self.classifier, fh)


if __name__ == '__main__':
    tr = TileRecognizer()
    tr.train_model(*tr.load_tiles())
    tr.persist_model()
