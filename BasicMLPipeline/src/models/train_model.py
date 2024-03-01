# src/models/train_model.py
import lightgbm as lgb
import pandas as pd
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def train_lightgbm_model(features, target):
    # Add your model training logic here
    # Example:
    params = {"objective": "regression", "metric": "rmse", "boosting_type": "gbdt"}
    train_data = lgb.Dataset(features, label=target)
    model = lgb.train(params, train_data)
    return model

def save_model(model, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    model.save_model(save_path)

if __name__ == "__main__":
    features_path = "../data/interim/dataset_features.csv"
    target_column = "target"
    model_save_path = "../models/lightgbm_model.txt"

    features = load_data(features_path)
    target = features.pop(target_column)

    trained_model = train_lightgbm_model(features, target)
    save_model(trained_model, model_save_path)
