import pandas as pd
import os
import zipfile

def clean_data():
    # Define file paths
    raw_data_zip_path = '/Users/saraafreen/Downloads/PanelStudyIncomeDynamics.csv.zip'
    raw_data_path = '/Users/saraafreen/Downloads/PanelStudyIncomeDynamics.csv'
    cleaned_data_path = 'data/cleaned/cleaned_PanelStudyIncomeDynamics.csv'

    # Unzip the CSV file
    with zipfile.ZipFile(raw_data_zip_path, 'r') as zip_ref:
        zip_ref.extractall('/Users/saraafreen/Downloads')  # Extract contents to Downloads folder
        print(f"{raw_data_path} has been extracted.")

    # Load the raw data
    df = pd.read_csv(raw_data_path)
    
    # Perform data cleaning (e.g., remove duplicates, fill missing values)
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)  # Replace missing values with 0

    # Save cleaned data
    os.makedirs('data/cleaned', exist_ok=True)
    df.to_csv(cleaned_data_path, index=False)
    print(f"Cleaned data saved to {cleaned_data_path}")

if __name__ == '__main__':
    clean_data()

