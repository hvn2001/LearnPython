import numpy as np

print('----A. Saving----')

arr = np.array([1, 2, 3])
# Saves to 'arr.npy'
np.save('arr.npy', arr)
# Also saves to 'arr.npy'
np.save('arr', arr)

print('----B. Loading----')
arr = np.array([1, 2, 3])
np.save('arr.npy', arr)
load_arr = np.load('arr.npy')
print(repr(load_arr))

# Will result in FileNotFoundError
# load_arr = np.load('arr')

print('----Ex: ----')


def save_points(save_file):
    points = np.random.uniform(
        low=-2.5, high=2.5, size=(100, 2))
    np.save(save_file, points)
