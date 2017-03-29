from sklearn import datasets  # For the iris dataset
from sklearn import tree  # For the Decision Tree classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split  # Handy for splitting data
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

# The data is x and the target is y because for a classifier f(x)=y
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)


dtc = tree.DecisionTreeClassifier()
dtc.fit(x_train, y_train)
predictions = dtc.predict(x_test)
# print(predictions)

print(f'Accuray for Decision Tree {accuracy_score(y_test, predictions)}')

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
predictions = knn.predict(x_test)

print(f'Accuray for K Nearest Neighbors {accuracy_score(y_test, predictions)}')
