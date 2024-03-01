# src/data/make_dataset.py
import pandas as pd
import os

def load_breast_cancer_data(raw_data_path):
  
    column_names = ['SampleCode', 'ClumpThickness', 'UniformityOfCellSize', 'UniformityOfCellShape', 
                        'MarginalAdhesion','SingleEpithelialCellSize', 'BareNuclei', 'BlandChromatin', 
                        'NormalNucleoli', 'Mitoses', 'Class']
    
    # Load Breast Cancer dataset using the provided column names
    return pd.read_csv(raw_data_path, header=None, names=column_names, na_values='?')

def save_dataset(processed_data, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    processed_data.to_csv(save_path, index=False)

if __name__ == "__main__":
    raw_data_path = "../../data/raw/breast_cancer_data.csv"
    processed_data_path = "../../data/processed/breast_cancer_processed.csv"

    raw_data = load_breast_cancer_data(raw_data_path)
    
    
    
    save_dataset(raw_data, processed_data_path)
