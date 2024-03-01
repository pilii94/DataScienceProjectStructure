# src/features/build_features.py
import pandas as pd
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def create_features(processed_data):
    # Add your feature engineering logic here
    # Example: processed_data['feature_sum'] = processed_data['feature1'] + processed_data['feature2']
    return processed_data

def save_features(features, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    features.to_csv(save_path, index=False)

if __name__ == "__main__":
    processed_data_path = "../data/processed/dataset_processed.csv"
    features_path = "../data/interim/dataset_features.csv"

    processed_data = load_data(processed_data_path)
    features = create_features(processed_data)
    save_features(features, features_path)
