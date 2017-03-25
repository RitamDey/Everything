from sklearn.datasets import load_iris  # Gets the testing datasets
from sklearn.tree import DecisionTreeClassifier
import numpy as np


iris = load_iris()  # Setsup the datasets

test_idx = [0, 50, 100]  # Seperate the testing data

# Training data
train_target = np.delete(iris.target, test_idx)  # Prepares Training features
train_data = np.delete(iris.data, test_idx, axis=0)  # Prepares the correct labels


# Testing data
test_target = iris.target[test_idx]  # Prepares testing features
test_data = iris.data[test_idx]  # Prepares the correct testing labels


clf = DecisionTreeClassifier()  # Creates the classifier
clf.fit(train_data,train_target)  # Trains it


print("The features of the flowers are ", iris.feature_names)
print("The labels for the flower are ", iris.target_names)

print("All the testing datas are ", *test_data)
print(f"All the testing flowers to be predicted are [0:'{iris.target_names[0]}' 1:'{iris.target_names[1]}' 2:'{iris.target_names[2]}']")
print(clf.predict(test_data))  # Predict the flowers
