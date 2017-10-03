import numpy as np
from sklearn.svm import SVC


rng = np.random.RandomState(0)
X = rng.rand(100, 10)
Y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)


clf = SVC()

# Hyper-parameters of an estimator can be updated via `sklearn.pipeline.Pipeline.set_params` 
# method. The `.fit()` needs to be called again to calibrate
clf.set_params(kernel='linear').fit(X, Y)
print(clf.predict(X_test))


clf.set_params(kernel='rbf').fit(X, Y)
print(clf.predict(X_test))
