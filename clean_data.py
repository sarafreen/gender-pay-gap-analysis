import pandas as pd
import os

def clean_data():
    # Load raw data
    raw_data_path = 'data/raw/dataset.csv'
    cleaned_data_path = 'data/cleaned/cleaned_dataset.csv'
    df = pd.read_csv(raw_data_path)
    
    # Perform data cleaning (e.g., remove duplicates, fill missing values)
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)  # Example for handling missing values
    
    # Save cleaned data
    os.makedirs('data/cleaned', exist_ok=True)
    df.to_csv(cleaned_data_path, index=False)
    print(f"Cleaned data saved to {cleaned_data_path}")
    
if __name__ == '__main__':
    clean_data()
