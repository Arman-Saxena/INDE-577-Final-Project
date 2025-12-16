import numpy as np

class LinearRegressionGD:

    def __init__(self, lr=0.01, n_iters=1000, verbose=False):
        self.lr = lr
        self.n_iters = n_iters
        self.verbose = verbose
        self.weights = None
        self.bias = 0
        self.loss_history = []

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for i in range(self.n_iters):

            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            loss = np.mean((y_pred - y)**2)
            self.loss_history.append(loss)

            if self.verbose and i % 500 == 0:
                print(f"Iteration {i}, Loss: {loss}")

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
