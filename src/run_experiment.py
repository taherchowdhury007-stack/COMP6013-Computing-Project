"""
Main entry point to run experiments end-to-end.

Pipeline:
Data -> Features -> Model -> Signal -> Backtest -> Evaluation
"""

from data_pipeline.download_data import download_stock_data
from features.build_features_daily import build_daily_features
from models.ml_model import MLModel
from backtesting.engine import BacktestEngine
from evaluation.metrics import calculate_metrics


def main():
    print("Running experiment pipeline...")


    # 1. Data Ingestion

    data = download_stock_data()


    # 2. Feature Engineering

    X, y = build_daily_features(data)


    # 3. Model Training

    model = MLModel()
    model.train(X, y)


    # 4. Backtesting

    engine = BacktestEngine()
    results = engine.run(model, X)


    # 5. Evaluation

    metrics = calculate_metrics(results)

    print("Pipeline structure successfully connected.")
    print("Evaluation metrics:", metrics)


if __name__ == "__main__":
    main()
