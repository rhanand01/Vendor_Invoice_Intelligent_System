import pandas as pd
import sqlite3 
from sklearn.model_selection import train_test_split
from pathlib import Path

def load_vendor_invoice_data(db_path:str):
    """
    Load vendor invoice data from SQLite database.
    """
    if db_path is None:
        db_path = Path(__file__).resolve().parents[1] / "Data" / "inventory.db"
    conn = sqlite3.connect(str(db_path))
    query = "select * from vendor_invoice"
    df = pd.read_sql_query(query,conn)
    conn.close
    return df

def prepare_feature(df:pd.DataFrame):
    """
    select feature and target variable.
    """
    X = df[['Quantity','Dollars']]
    y = df['Freight']
    return X, y

def split_data(X,y, test_size = 0.2, random_state = 42):
    """
    split dataset into train and test sets.
    """
    return train_test_split(
        X, y, 
        test_size = 0.2,
        random_state = 42
    )
    
     