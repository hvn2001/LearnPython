from tensorflow.python.keras.models import Sequential
from tensorflow.python.layers.core import Dense

print('------A. Configuring for training------')

model = Sequential()
layer1 = Dense(5, activation='relu', input_dim=4)
model.add(layer1)
layer2 = Dense(1, activation='sigmoid')
model.add(layer2)
model.compile('adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print('------Ex: ------')

model = Sequential()
layer1 = Dense(5, activation='relu', input_dim=2)
model.add(layer1)
layer2 = Dense(5, activation='relu')
model.add(layer2)
layer3 = Dense(3, activation='softmax')
model.add(layer3)
model.compile('adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
