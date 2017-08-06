from sklearn import tree


# Dataset
# [size, weight, texture]
X = [
        [181, 80, 44],
        [177, 70, 43],
        [160, 60, 38],
        [154, 54, 37],
        [166, 65, 40],
        [190, 90, 47],
        [175, 64, 39],
        [177, 70, 40],
        [159, 55, 37],
        [171, 75, 42],
        [181, 85, 43]
    ]


Y = [
        'apple',
        'apple',
        'orange',
        'orange',
        'apple',
        'apple',
        'orange',
        'orange',
        'orange',
        'apple',
        'apple'
    ]


# Classifier is Decision Tree
clf_tree = tree.DecisionTreeClassifier()
clf_tree = clf_tree.fit(X, Y)


# Test Data
test_data = [[190, 70, 42], [172, 64, 39], [182, 80, 42]]


# Predict
prediction_tree = clf_tree.predict(test_data)


print("Prediction of Decision Tree Classifier:", prediction_tree)
