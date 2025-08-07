import pandas as pd

def load_datafile(file_path:str, max_number_rows) -> pd.DataFrame:
    """
    Load a data file into a pandas DataFrame.
    
    Args:
        file_path (str): The path to the data file.
        
    Returns:
        pd.DataFrame: The loaded data as a DataFrame.
    """
    try:
        df = pd.read_csv(file_path,nrows=max_number_rows)
        return df
    except Exception as e:
        print(f"Error loading data file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error