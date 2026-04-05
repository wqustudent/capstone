import pandas as pd


class FeatureEngineer:
    def __init__(self):
        self.df = None

    def engineer_features(self, data: pd.DataFrame) -> pd.DataFrame:
        self.df = data
        self._add_standard_features()
        self._add_cross_instrument_features()
        self._add_fractal_features()

        return self.df

    def _add_standard_features(self):
        pass

    def _add_cross_instrument_features(self):
        pass

    def _add_fractal_features(self):
        pass


if __name__ == "__main__":
    df = pd.DataFrame()  # can fetch from data_wrangler.py
    worker = FeatureEngineer()
    worker.engineer_features(df)
    print(df)
