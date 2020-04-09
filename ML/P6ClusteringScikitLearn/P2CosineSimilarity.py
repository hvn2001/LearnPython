import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model

print('------B. Calculating cosine similarity------')

from sklearn.metrics.pairwise import cosine_similarity

data = np.array([
    [1.1, 0.3],
    [2.1, 0.6],
    [-1.1, -0.4],
    [0., -3.2]])
cos_sims = cosine_similarity(data)
print('{}\n'.format(repr(cos_sims)))
'''
array([[ 1.        ,  0.99992743, -0.99659724, -0.26311741],
       [ 0.99992743,  1.        , -0.99751792, -0.27472113],
       [-0.99659724, -0.99751792,  1.        ,  0.34174306],
       [-0.26311741, -0.27472113,  0.34174306,  1.        ]])
'''
print('------B. cosine_similarity------')

from sklearn.metrics.pairwise import cosine_similarity

data = np.array([
    [1.1, 0.3],
    [2.1, 0.6],
    [-1.1, -0.4],
    [0., -3.2]])
data2 = np.array([
    [1.7, 0.4],
    [4.2, 1.25],
    [-8.1, 1.2]])
cos_sims = cosine_similarity(data, data2)
print('{}\n'.format(repr(cos_sims)))
'''
array([[ 0.9993819 ,  0.99973508, -0.91578821],
       [ 0.99888586,  0.99993982, -0.9108828 ],
       [-0.99308366, -0.9982304 ,  0.87956492],
       [-0.22903933, -0.28525359, -0.14654866]])

'''

print('------Ex: ------')
cos_sims = cosine_similarity(data)  # Ex1
np.fill_diagonal(cos_sims, 0)  # Ex2
similar_indexes = cos_sims.argmax(axis=1)  # Ex3
