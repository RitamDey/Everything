from sklearn import datasets
from sklearn.svm import SVC


iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)

print(clf.predict(iris.data[:3]))  # Returns integer array as iris.target is integer array


clf.fit(iris.data, iris.target_names[iris.target])


print(clf.predict(iris.data[:3]))  # Returns string array as we used names array
