from file_operation import *
import pandas as pd

print('-----\n1.物品管理')

m = int(input())

if m == 1:
    while True:
        df = read_file_as_Dataframe('items.csv')
        if isinstance(df, int) and df == -1:
            print('没有items文件。创建了默认格式items文件。')
            create_default_empty_CSV('items.csv')
            df = read_file_as_Dataframe('items.csv')

        print('-----\n1.增加物品\n2.减少物品\n3.退出并保存')
        choice = int(input())
        if choice == 3:
            #save file
            break

