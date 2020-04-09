from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense

print('------Adding two Dense layers to a Sequential model------')
model = Sequential()
layer1 = Dense(5, input_dim=4)
model.add(layer1)
layer2 = Dense(3, activation='relu')
model.add(layer2)

print('------Initializing a Sequential model with two Dense layers------')
layer1 = Dense(5, input_dim=4)
layer2 = Dense(3, activation='relu')
model = Sequential([layer1, layer2])

print('------Ex1------')
model = Sequential()
print('------Ex2------')
layer1 = Dense(5, activation='relu', input_dim=2)
model.add(layer1)
