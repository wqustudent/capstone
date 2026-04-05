from workers.data_wrangler import DataWrangler
from workers.feature_engineer import FeatureEngineer
from workers.knn_estimator import KNNEstimator


def run_pipeline():
    wrangler = DataWrangler()
    df = wrangler.preprocess()

    feature_engineer = FeatureEngineer(df)
    df = feature_engineer.engineer_features()

    y = df['target']
    estimator = KNNEstimator(df, y)
    estimator.fit()
    y_hat = estimator.predict()
    print(y_hat)


if __name__ == '__main__':
    run_pipeline()

