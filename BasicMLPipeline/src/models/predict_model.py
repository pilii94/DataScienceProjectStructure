# src/models/predict_model.py
import lightgbm as lgb
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def load_model(model_path):
    return lgb.Booster(model_file=model_path)

def make_predictions(model, features):
    # Add your prediction logic here
    # Example: predictions = model.predict(features)
    return predictions

if __name__ == "__main__":
    features_path = "../data/interim/dataset_features.csv"
    model_path = "../models/lightgbm_model.txt"
    predictions_save_path = "../reports/predictions.csv"

    features = load_data(features_path)
    trained_model = load_model(model_path)

    predictions = make_predictions(trained_model, features)
    predictions.to_csv(predictions_save_path, index=False)
