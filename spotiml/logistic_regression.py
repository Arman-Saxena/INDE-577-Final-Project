import numpy as np

class LogisticRegressionGD:
    def __init__(self, lr=0.01, n_iters=5000, verbose=False):
        self.lr = lr
        self.n_iters = n_iters
        self.verbose = verbose
        self.loss_history = []

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def compute_loss(self, y, y_hat):
        eps = 1e-9
        return -np.mean(y * np.log(y_hat + eps) + (1 - y) * np.log(1 - y_hat + eps))

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for i in range(self.n_iters):
            linear_pred = X @ self.weights + self.bias
            y_hat = self.sigmoid(linear_pred)

            dw = (1 / n_samples) * (X.T @ (y_hat - y))
            db = (1 / n_samples) * np.sum(y_hat - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            loss = self.compute_loss(y, y_hat)
            self.loss_history.append(loss)

            if self.verbose and i % 500 == 0:
                print(f"Iteration {i}, Loss = {loss:.4f}")

    def predict(self, X):
        y_hat = self.sigmoid(X @ self.weights + self.bias)
        return (y_hat >= 0.5).astype(int)
