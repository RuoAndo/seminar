# coding: utf-8

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import np_utils

#from keras import Sequential
#from keras import Dense, Activation
#from keras import np_utils
import numpy as np

data = np.random.random((1000, 784))
labels = np.random.randint(10, size=(1000, 1))
labels = np_utils.to_categorical(labels, 10)

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=784))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop', 
             loss='categorical_crossentropy', 
             metrics=['accuracy'])

model.fit(data, labels)
