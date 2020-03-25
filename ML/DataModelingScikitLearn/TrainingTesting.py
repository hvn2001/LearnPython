import numpy as np

print('------B. Splitting the dataset------')

data = np.array([
    [10.2, 0.5],
    [8.7, 0.9],
    [9.3, 0.8],
    [10.1, 0.4],
    [9.5, 0.77],
    [9.1, 0.68],
    [7.7, 0.9],
    [8.3, 0.8]])
labels = np.array(
    [1.4, 1.2, 1.6, 1.5, 1.6, 1.3, 1.1, 1.2])

from sklearn.model_selection import train_test_split

split_dataset = train_test_split(data, labels)
train_data = split_dataset[0]
test_data = split_dataset[1]
train_labels = split_dataset[2]
test_labels = split_dataset[3]

print('{}\n'.format(repr(train_data)))
print('{}\n'.format(repr(train_labels)))
print('{}\n'.format(repr(test_data)))
print('{}\n'.format(repr(test_labels)))

'''
array([[ 8.7 ,  0.9 ],
       [ 7.7 ,  0.9 ],
       [ 9.5 ,  0.77],
       [10.2 ,  0.5 ],
       [10.1 ,  0.4 ],
       [ 9.1 ,  0.68]])

array([1.2, 1.1, 1.6, 1.4, 1.5, 1.3])
'''

print('------B. test_size------')
data = np.array([
    [10.2, 0.5],
    [8.7, 0.9],
    [9.3, 0.8],
    [10.1, 0.4],
    [9.5, 0.77],
    [9.1, 0.68],
    [7.7, 0.9],
    [8.3, 0.8]])
labels = np.array(
    [1.4, 1.2, 1.6, 1.5, 1.6, 1.3, 1.1, 1.2])

from sklearn.model_selection import train_test_split

split_dataset = train_test_split(data, labels,
                                 test_size=0.375)
train_data = split_dataset[0]
test_data = split_dataset[1]
train_labels = split_dataset[2]
test_labels = split_dataset[3]

print('{}\n'.format(repr(train_data)))
print('{}\n'.format(repr(train_labels)))
print('{}\n'.format(repr(test_data)))
print('{}\n'.format(repr(test_labels)))

print('------Ex: ------')


def dataset_splitter(data, labels, test_size=0.25):
    split_dataset = train_test_split(data, labels,
                                     test_size=test_size)
    train_set = (split_dataset[0], split_dataset[2])
    test_set = (split_dataset[1], split_dataset[3])
    return train_set, test_set
