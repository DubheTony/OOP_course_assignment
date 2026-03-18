import numpy as np
import pandas as pd
import os
from typing import Dict

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

def load_all_csv(data_dir):
    """
    扫描所有 .csv 文件，返回 {类名: DataFrame} 字典。
    """
    dataframes = {}
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            class_name = filename[:-4]
            file_path = os.path.join(data_dir, filename)
            try:
                df = pd.read_csv(file_path)
                dataframes[class_name] = df
                print(f"加载 {class_name}")
            except Exception as e:
                print(e)
    return dataframes


def save_objects_to_csv(objects_by_type):
    for type_name, obj_list in objects_by_type.items():
        data = [obj.__dict__ for obj in obj_list]
        df = pd.DataFrame(data)
        file_path = f'.{type_name}.csv'
        df.to_csv(file_path)
    return 0