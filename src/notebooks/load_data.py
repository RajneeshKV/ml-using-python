import pandas as pd
import numpy as np

def load_csvdata(file_path):
    """
    Load data from a CSV file and return a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None