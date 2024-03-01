# src/data/download_data.py
import urllib.request
import os

def download_breast_cancer_data(save_path, column_names_path):
    # Breast Cancer dataset URL
    breast_cancer_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
    
    # Column names URL
    column_names_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.names"
    
    # Download Breast Cancer dataset
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    urllib.request.urlretrieve(breast_cancer_url, save_path)
    
    # Download column names
    os.makedirs(os.path.dirname(column_names_path), exist_ok=True)
    urllib.request.urlretrieve(column_names_url, column_names_path)

if __name__ == "__main__":
    breast_cancer_raw_path = "../../data/raw/breast_cancer_data.csv"
    column_names_path = "../../data/raw/breast_cancer_column_names.txt"
    
    download_breast_cancer_data(breast_cancer_raw_path, column_names_path)
