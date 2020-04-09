from tensorflow.python.keras.models import Sequential
from tensorflow.python.layers.core import Dense
from numpy import np

data = np.array([
    [5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.9, 3., 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.7, 3.2, 1.3, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
    [4.6, 3.1, 1.5, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5, 1.4,
     0.2, 5.1, 3.5, 1.4, 0.2, 5.1, 3.5],
])
labels = np.array([0, 1, 0, 1])
print('------A. Training------')

model = Sequential()
layer1 = Dense(200, activation='relu', input_dim=4)
model.add(layer1)
layer2 = Dense(200, activation='relu')
model.add(layer2)
layer3 = Dense(3, activation='softmax')
model.add(layer3)
model.compile('adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# predefined multiclass dataset
train_output = model.fit(data, labels,
                         batch_size=20, epochs=5)

print('---------------------')
print(train_output.history)

print('------B. Evaluation------')
# predefined eval dataset
print(model.evaluate(eval_data, eval_labels))

print('------C. Predictions------')
# 3 new data observations
print('{}'.format(repr(model.predict(new_data))))
