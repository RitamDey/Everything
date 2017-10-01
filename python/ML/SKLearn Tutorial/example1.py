from sklearn import datasets
from sklearn import svm


digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100.)  # Create a Support Vector Classifier
clf.fit(digits.data[:-1], digits.target[:-1])  # Train the classifier

print(clf.predict(digits.data[-1:]))  # Predict the digit
