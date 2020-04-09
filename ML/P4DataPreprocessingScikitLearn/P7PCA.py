import pandas as pd

print('------B. PCA in scikit-learn------')
data = pd.DataFrame({'HR': [1.5, 2.2, 3., 8.],
                     'HR2': [3., 4.3, 6.1, 16.],
                     'HR4': [9., 3.5, 1.1, 7.7],
                     'HR5': [-0.5, 0.6, 1.2, -1.],
                     'HR6': [1., 2.7, 4.2, 7.1]})
print('{}\n'.format(repr(data)))

from sklearn.decomposition import PCA

pca_obj = PCA()  # The value of n_component will be 4. As m is 5 and default is always m-1
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

pca_obj = PCA(n_components=3)
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

pca_obj = PCA(n_components=2)
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

'''
array([[ 1.5,  3. ,  9. , -0.5,  1. ],
       [ 2.2,  4.3,  3.5,  0.6,  2.7],
       [ 3. ,  6.1,  1.1,  1.2,  4.2],
       [ 8. , 16. ,  7.7, -1. ,  7.1]])

array([[-4.8600e+00,  4.6300e+00, -4.7000e-02,  0.0000e+00],
       [-3.7990e+00, -1.3180e+00,  1.2700e-01,  0.0000e+00],
       [-1.8630e+00, -4.2260e+00, -8.9000e-02,  0.0000e+00],
       [ 1.0522e+01,  9.1400e-01,  9.0000e-03,  0.0000e+00]])

array([[-4.8600e+00,  4.6300e+00, -4.7000e-02],
       [-3.7990e+00, -1.3180e+00,  1.2700e-01],
       [-1.8630e+00, -4.2260e+00, -8.9000e-02],
       [ 1.0522e+01,  9.1400e-01,  9.0000e-03]])

array([[-4.86 ,  4.63 ],
       [-3.799, -1.318],
       [-1.863, -4.226],
       [10.522,  0.914]])
'''

print('------Ex: ------')


def pca_data(data, n_components):
    pca_obj = PCA(n_components=n_components)
    component_data = pca_obj.fit_transform(data)
    return component_data
