import numpy as np

class KNNClassifier:

    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict_one(self, x):
        distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
        idx = np.argsort(distances)[:self.k]
        nearest_labels = self.y_train[idx]
        return np.round(nearest_labels.mean()).astype(int)

    def predict(self, X):
        return np.array([self.predict_one(x) for x in X])
