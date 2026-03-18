from file_operation import *
import Item
import sys
import pandas as pd

# --------------------------------------------------------------------------

# 物品类型列表
itemsList = ['Fruit','Drink']

dataframes = {}
objects_type_dict = {}

for i in itemsList:
    # 按food、drink等类别，分csv存储，
    # 和转化为DF
    filename = f'{i}.csv'
    df = read_file_as_Dataframe(filename)
    if isinstance(df, int) and df == -1:
        print(f'没有{i}文件。创建了默认格式{i}文件。')
        create_default_empty_CSV(filename)
        df = read_file_as_Dataframe(filename)
    dataframes[i] = df

for type_name, df in dataframes.items():
    cls = getattr(Item, type_name)
    objects = [cls(**row.to_dict()) for _, row in df.iterrows()]
    objects_type_dict[type_name] = objects

while True:
    print('---------------------------')
    print('1.物品管理')
    print('0.退出')
    print('---------------------------')

    m = int(input())
    if m == 0:
        break
    elif 1 <= m <= len(itemsList):
        while True:
            print('\n可管理的物品类型：')
            for idx, item in enumerate(itemsList, 1):
                print(f'{idx}.{item}')
            print(f'{len(itemsList)+1}.返回上一级')
            type_choice = int(input('请选择物品类型：'))
            if type_choice == len(itemsList)+1:
                break
            else:
                selected_type = itemsList[type_choice - 1]
                obj_list = objects_type_dict[selected_type]

            while True:
                print(f'-------------{selected_type}-------------')
                print('1.增加物品\n2.减少物品\n3.退出并保存')
                print('---------------------------')

                choice1 = int(input())
                if choice1 == 1:
                    pass
                elif choice1 == 2:
                    pass
                elif choice1 == 3:
                    save_objects_to_csv(objects_type_dict)
                    break
    else:
         print('无效选择')


save_objects_to_csv(objects_type_dict)

sys.exit('退出程序')
