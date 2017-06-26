from sklearn.datasets import load_iris
import numpy as np


data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']


plength = features[:, 2]
# use numpy operations to get setosa features
is_setosa = (labels == 'setosa')
# This is the important step
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print(f'Maximum of setosa: {max_setosa}')
print(f'Minimum of others: {min_non_setosa}')
