#!/usr/bin/env python3

'''Run this to train the models
'''

from __future__ import print_function
from keras.utils.data_utils import get_file
from keras.callbacks import ModelCheckpoint
import numpy as np
import random
import sys
import importlib


VERSION = sys.argv[1]
path = sys.argv[2]
DATASET = path.split('/')[2]
text = open(path).read().lower()

print('corpus length:', len(text))


chars = sorted(list(set(text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


print('Build model...')
module = importlib.import_module(('.'.join(sys.argv[3].split('/'))))
get_model = getattr(module, 'get_model')
model = get_model(maxlen, len(chars))

best_validation = float("inf")
for iteration in range(1, 30):
        print('Iteration Number', iteration)
        hist = model.fit(X, y, batch_size=128, nb_epoch=1, validation_split=0.2)
        print(hist.history)
        if best_validation > hist.history['val_loss'][0]:
            best_validation = hist.history['val_loss'][0]
            print('Best model so far. Saving...')
            model.save('../trained_models/' + DATASET + '_' + VERSION + '.h5')
