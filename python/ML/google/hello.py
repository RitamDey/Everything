from sklearn.tree import DecisionTreeClassifier

# 0 is orange and bumpy, while 1 is apple and smooth

features = [[140, 1], [130, 1], [150, 0], [170, 0]]  # Training data: features of fruits
labels = [0, 0, 1, 1]  # Training data: labels for fruits


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)  # Training the classifier
print(clf.predict([[150, 0]]))  # Give it some data to predict
