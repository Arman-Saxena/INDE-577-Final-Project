import numpy as np
from collections import Counter

class KNN:
    """
    K-Nearest Neighbors Classification (manual).
    """

    def __init__(self, k=5):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _distance(self, a, b):
        return np.sqrt(np.sum((a - b)**2))

    def predict(self, X):
        preds = []
        for point in X:
            distances = [self._distance(point, x_train) for x_train in self.X_train]
            
            # get k nearest neighbors
            k_idx = np.argsort(distances)[:self.k]
            k_neighbor_labels = [self.y_train[i] for i in k_idx]

            # majority vote
            most_common = Counter(k_neighbor_labels).most_common(1)[0][0]
            preds.append(most_common)
        return np.array(preds)
