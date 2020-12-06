import os
import pickle

import numpy
from PIL import Image
from sklearn import svm


class TileRecognizer:
    def __init__(self):
        self.classifier = svm.SVC(gamma=0.001, C=100)

    def load_tiles(self):
        # TODO: This should really pull from a well defined training data location
        tiles, labels = [], []
        for file in os.listdir('tiles-labelled'):
            image = Image.open(f'tiles-labelled/{file}')
            tile = tile_to_datapoint(image)
            label = int(file.split('-')[1].split('.')[0])
            tiles.append(tile)
            labels.append(label)
        return numpy.array(tiles), labels

    def train_model(self, data, labels):
        # TODO: Possibly read training data from object
        self.classifier.fit(data, labels)

    def persist_model(self):
        with open('tile_recognizer.pickle', 'wb') as fh:
            pickle.dump(self.classifier, fh)


def tile_to_datapoint(tile: Image, resolution=20):
    dimensions = (resolution, round(resolution * 1.5))
    tile = tile.convert(mode='L').resize(dimensions)
    return numpy.asarray(tile).flatten()


if __name__ == '__main__':
    tr = TileRecognizer()
    tr.train_model(*tr.load_tiles())
    tr.persist_model()
