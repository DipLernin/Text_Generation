#!/usr/bin/env python3

from __future__ import print_function
from keras.utils.data_utils import get_file
from keras.callbacks import ModelCheckpoint
import numpy as np
import random
import sys
import importlib
import pandas as pd

path = '../Text_Generation/datasets/poems.txt'
text = open(path, encoding = "ISO-8859-1").read().lower()

chars = sorted(list(set(text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))


X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

all_opt = [ 'sgd',
        'rmsprop',
        'adagrad',
        'adadelta',
        'adam',
        'adamax',
        'nadam']


from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
from keras.optimizers import RMSprop

model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

for opt in  all_opt:
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    hist = model.fit(X, y, batch_size=128, nb_epoch=10, validation_split=0.2)
    df = pd.DataFrame.from_dict(hist.history, orient='columns')
    df.to_csv('ver_log'+str(opt), sep=',', encoding='utf-8', index=False)
