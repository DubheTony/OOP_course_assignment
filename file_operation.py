import numpy as np
import pandas as pd
from pathlib import Path

def read_file_as_Dataframe(fileName):
    try:
        df1 = pd.read_csv(fileName)
        return df1
    except FileNotFoundError:
        return -1

def create_default_empty_CSV(fileName):
    df = pd.DataFrame(columns=['Name', 'Number','Manufacturing_Date','Best_Before_Date','Shelf_Life'])
    df.to_csv(fileName, index=False, encoding='utf-8')
    return 0