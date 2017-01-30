# One layer LSTM

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop

def get_model(maxlen, len_chars):
    model = Sequential()
    model.add(LSTM(128, input_shape=(maxlen, len_chars), dropout_W=0.5, dropout_U=0.5))
    model.add(Dropout(0.5))
    model.add(Dense(len_chars))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam',  metrics=['accuracy'])
    return model
