import pandas as pd


class KNNEstimator:
    def __init__(self, X: pd.DataFrame, y: pd.Series):
        self.X = X
        self.y = y
        self.distance = "euclidean"

    def fit(self):
        # TODO: fit X, y
        pass

    def predict(self):
        # TODO: predict X
        pass

    def score(self):
        # TODO: score using X & y
        pass

    def _lorentzian_distance(self, X, y):
        # TODO: define lorentzian distance
        pass

    def _euclidian_distance(self, X, y):
        # TODO: define euclidian distance
        pass


if __name__ == "__main__":
    X = pd.DataFrame()  # can fetch from feature_engineer.py
    y = pd.Series()  # known/target column of X
    worker = KNNEstimator(X, y)
    worker.fit()
    worker.predict()
    worker.score()
