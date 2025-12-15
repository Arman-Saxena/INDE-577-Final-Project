import numpy as np

class KMeans:
    """
    K-Means clustering from scratch.
    """

    def __init__(self, k=3, max_iters=300):
        self.k = k
        self.max_iters = max_iters

    def fit(self, X):
        n_samples, n_features = X.shape

        # randomly initialize centroids from samples
        np.random.seed(42)
        random_idx = np.random.choice(n_samples, self.k, replace=False)
        self.centroids = X[random_idx]

        for _ in range(self.max_iters):
            # assign clusters
            clusters = self._assign_clusters(X)

            # compute new centroids
            new_centroids = np.array([X[clusters == i].mean(axis=0) for i in range(self.k)])

            # check convergence
            if np.all(new_centroids == self.centroids):
                break

            self.centroids = new_centroids

        self.labels_ = self._assign_clusters(X)

    def _assign_clusters(self, X):
        distances = np.array([np.linalg.norm(X - centroid, axis=1) for centroid in self.centroids])
        return np.argmin(distances, axis=0)

    def predict(self, X):
        distances = np.array([np.linalg.norm(X - centroid, axis=1) for centroid in self.centroids])
        return np.argmin(distances, axis=0)
