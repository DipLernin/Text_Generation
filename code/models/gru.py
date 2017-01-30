# GRU (Gated Recurrent Unit): it is supposed to work similar as LSTM but to be more efficient

from keras.models import Sequential
from keras.layers import Dense, Activation, GRU
from keras.optimizers import RMSprop


def get_model(maxlen, len_chars):
    model = Sequential()
    model.add(GRU(128, input_shape=(maxlen, len_chars)))
    model.add(Dense(len_chars))
    model.add(Activation('softmax'))
    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer,  metrics=['accuracy'])
    return model
