# coding: utf-8

import numpy as np
import pandas as pd
import sqlalchemy

'''
pandas 数据中的None 和NaN的判断
'''


def com(row):
    if pd.isnull(row["A"]):
        return 0
    else:
        return 1


def com_none(row):
    if pd.isnull(row["C"]):
        return 0
    else:
        return 1


df = pd.DataFrame({"A": [1, np.nan], "C": None})
print(df)
print(np.nan)

df["B"] = df.apply(lambda row: com(row), axis=1)
print(df)

df["D"] = df.apply(lambda row: com_none(row), axis=1)
print(df)

'''
Nan 和None 存入mysqldb
'''

edwdata_engine = sqlalchemy.create_engine(
    "mysql+mysqlconnector://root:123456@192.168.1.139/temp?charset=utf8")

df.to_sql("nan_data", edwdata_engine, if_exists='replace', index=False)