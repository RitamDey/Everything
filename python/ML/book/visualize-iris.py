from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np


# Load the dataset
data = load_iris()

# Get features
features = data['data']

# Get feature names
feature_names = data['feature_names']

# Get the targets
target = data['target']


for t, marker, c in zip(range(3), '>ox', 'rgb'):
    # Plot the data in differnt colors
    obj = plt.scatter(
        features[target == t, 0],
        features[target == t, 1],
        marker=marker,
        c=c
    )

    obj.show()
