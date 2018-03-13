# coding: utf-8

import uuid
import random
from datetime import datetime
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)
pd.options.display.max_colwidth = 0

num = 150000
print("1:{}".format(datetime.now()))
dic = {str(uuid.uuid1()): random.randint(1, 2880) for i in range(0, num)}
print("2:{}".format(datetime.now()))
# dic = dic[0]
print("3:{}".format(datetime.now()))
# print(dic)
print("4:{}".format(datetime.now()))
try:
    a = dic["820a789d-62b7-11e7-a758-74dfbfb2c6ee"]
except:
    print("5:{}".format(datetime.now()))

print("66:{}".format(datetime.now()))

test_data = pd.DataFrame(
    {
        'company_guid': [str(uuid.uuid1()) for i in range(0, num)],
        'rereview_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'answer_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'close_query_query_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'allocate_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'first_read_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'second_read_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'judge_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'a': [random.randint(1, 2880) for i in range(0, num)],
        'b': [random.randint(1, 2880) for i in range(0, num)],
        'c': [random.randint(1, 2880) for i in range(0, num)],
        'd': [random.randint(1, 2880) for i in range(0, num)],
        'e': [random.randint(1, 2880) for i in range(0, num)],
        'f': [random.randint(1, 2880) for i in range(0, num)],
        'g': [random.randint(1, 2880) for i in range(0, num)],
        'q': [random.randint(1, 2880) for i in range(0, num)],
        'w': [random.randint(1, 2880) for i in range(0, num)],
        'e': [random.randint(1, 2880) for i in range(0, num)],
        'r': [random.randint(1, 2880) for i in range(0, num)],
        't': [random.randint(1, 2880) for i in range(0, num)],
        'y': [random.randint(1, 2880) for i in range(0, num)],
        'u': [random.randint(1, 2880) for i in range(0, num)],

    }
)
import sqlalchemy

rawdata_pv_engine = sqlalchemy.create_engine(
    "mysql+mysqlconnector://root:123456@192.168.1.139:3306/raw_big_pv?charset=utf8")

sql_text = "select Id,Name_chs from Items"
items_info = pd.read_sql(sql_text, rawdata_pv_engine)
# items_info.set_index(["Id"])
dic = {row["Id"]: row for index, row in items_info.iterrows()}


# items_dict = {row["Id"]: row for index, row in test_data.iterrows()}

# dic = {row["company_guid"]: row for index, row in test_data.iterrows()}


def dic_get(item_id, dic):
    # print("dic1:{}".format(datetime.now()))
    a = "kjkjk"
    # try:
    #     a = dic.get(item_id)["close_query_query_avg_duration"]
    # except:
    #     pass
    print("test_00_start:---------,{}".format(datetime.now()))
    # if item_id in dic:
    #     a = dic[item_id]["Name_chs"]

    m=dic.get(item_id)
    # print("dic2:{}".format(datetime.now()))
    print("test_00_end:---------,{}".format(datetime.now()))
    return a


def dict_new(row, columns):
    m = []
    for column in columns:
        m.append(row[column] + 1)

    return pd.Series(m)


def dic_m(row, columns):
    m = []
    for column in columns:
        m.append(dic.get("company_guid"))
        # dic.get("company_guid")

    # return ""
    return pd.Series(np.array(m))


def transform_items_cn(data_info, transform_columns):
    for column in transform_columns:
        print("test_00_start:{},{}".format(datetime.now(), column))
        data_info[column] = data_info.apply(
            lambda row: dic_get("ui", dic), axis=1)
        print("test_00_end:{},{}".format(datetime.now(), column))

    return data_info


columns = ["close_query_query_avg_duration", "allocate_avg_duration", "second_read_avg_duration"]

# print(test_data)
#
# test_data[columns] = test_data.apply(
#     lambda row: dict_new(row, columns), axis=1)
#
# print(test_data)
# print("1112:{}".format(datetime.now()))

# print("test_m:{}".format(datetime.now()))
# test_m = test_data.apply(
#     lambda row: dic_m(row, columns), axis=1)
# print("test_m_end:{}".format(datetime.now()))

# test_m = test_m.to_frame().reset_index()
# print(test_m.columns)
# print(test_m)
# print(type(test_data))
# print(type(test_m))

print("test_l:{}".format(datetime.now()))
transform_items_cn(test_data, columns)
print("test_l_end:{}".format(datetime.now()))

print(np.array(columns))
