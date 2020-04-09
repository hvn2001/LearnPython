import numpy as np

print('----A. Random integers----')
print(np.random.randint(5))
print(np.random.randint(5))
print(np.random.randint(5, high=6))  # 5 only !

random_arr = np.random.randint(-3, high=14,
                               size=(2, 2))
print(repr(random_arr))

print('----B. Utility functions----')
np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(repr(random_arr))

# New seed
np.random.seed(2)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(repr(random_arr))

# Original seed
np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(repr(random_arr))

print('----B. np.random.shuffle----')
vec = np.array([1, 2, 3, 4, 5])
np.random.shuffle(vec)
print(repr(vec))
np.random.shuffle(vec)
print(repr(vec))

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
np.random.shuffle(matrix)
print(repr(matrix))

print('----C. Distributions----')
print(np.random.uniform())
print(np.random.uniform(low=-1.5, high=2.2))
print(repr(np.random.uniform(size=3)))
print(repr(np.random.uniform(low=-3.4, high=5.9,
                             size=(2, 2))))

print('----C. np.random.normal----')
print(np.random.normal())
print(np.random.normal(loc=1.5, scale=3.5))
print(repr(np.random.normal(loc=-2.4, scale=4.0,
                            size=(2, 2))))

print('----D. Custom sampling----')
colors = ['red', 'blue', 'green']
print(np.random.choice(colors))
print(repr(np.random.choice(colors, size=2)))
print(repr(np.random.choice(colors, size=(2, 2),
                            p=[0.8, 0.19, 0.01])))

print('----Ex----')
random1 = np.random.randint(5)
random_arr = np.random.randint(3, high=10, size=(3, 5))


random_uniform = np.random.uniform(low=-2.5, high=1.5, size=5)


random_norm = np.random.normal(loc=2.0, scale=3.5, size=(10, 5))


choices = ['a', 'b', 'c', 'd']
choice = np.random.choice(choices, p=[0.5, 0.1, 0.2, 0.2])

arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)

