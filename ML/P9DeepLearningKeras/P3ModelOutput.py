from tensorflow.python.keras.models import Sequential
from tensorflow.python.layers.core import Dense

print('------Creating an MLP model for binary classification (sigmoid activation)------')
model = Sequential()
layer1 = Dense(5, activation='relu', input_dim=4)
model.add(layer1)
layer2 = Dense(1, activation='sigmoid')
model.add(layer2)

print('------Creating an MLP model for multiclass classification with 3 classes (softmax activation)..------')
model = Sequential()
layer1 = Dense(5, input_dim=4)
model.add(layer1)
layer2 = Dense(3, activation='softmax')
model.add(layer2)

print('------Ex: ------')
model = Sequential()
layer1 = Dense(5, activation='relu', input_dim=2)
model.add(layer1)
layer2 = Dense(5, activation='relu')
model.add(layer2)
layer3 = Dense(3, activation='softmax')
model.add(layer3)
