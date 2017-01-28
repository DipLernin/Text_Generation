# Two layer LSTM

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.layers import Dropout
from keras.optimizers import RMSprop

def get_model(maxlen, len_chars):
    model = Sequential()
    model.add(LSTM(256, input_shape=(maxlen, len_chars), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(128, input_shape=(len_chars, len_chars)))
    model.add(Dense(len_chars))
    model.add(LSTM(128, input_shape=(len_chars, len_chars)))
    model.add(Activation('softmax'))
    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer,  metrics=['accuracy'])
    return model