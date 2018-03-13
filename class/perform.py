# coding: utf-8

import uuid
import random
from datetime import datetime
import pandas as pd
import timeit

num = 100
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
        'judge_avg_duration': [random.randint(1, 2880) for i in range(0, num)]
    }
)

pd_data = pd.DataFrame(
    {
        'company_guid': [str(uuid.uuid1()) for i in range(0, num)],
        'rereview_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'answer_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'close_query_query_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'allocate_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'first_read_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'second_read_avg_duration': [random.randint(1, 2880) for i in range(0, num)],
        'judge_avg_duration': [random.randint(1, 2880) for i in range(0, num)]
    }
)


def dic_get(item_id, dic):
    # print("dic1:{}".format(datetime.now()))
    try:
        a = dic[item_id]
    except:
        pass
    # print("dic2:{}".format(datetime.now()))
    return "kjkjk"


def pd_get(item_id, pd_data):
    # print("pd1:{}".format(datetime.now()))
    one_data = pd_data.loc[pd_data["company_guid"] == item_id]
    # print("pd2:{}".format(datetime.now()))
    # print("88:{}".format(datetime.now()))
    # if len(one_data) > 0:
    #     print("exist")
    # else:
    #     print("not exist")
    return "jkjkjk"


dicts = {row["company_guid"]: row for index, row in pd_data.iterrows()}

for index, row in pd_data.iterrows():
    print(row["company_guid"], row)

# print("77:{}".format(datetime.now()))
# one_data = pd_data.loc[pd_data["company_guid"] == "sdfs"]
# print("88:{}".format(datetime.now()))
# if len(one_data) > 0:
#     print("exist")
# else:
#     print("not exist")
# print("99:{}".format(datetime.now()))

# print("1111:{}".format(datetime.now()))
#
test_data["dic_name"] = test_data.apply(
    lambda row: dic_get(row["company_guid"], dic), axis=1)
print("1112:{}".format(datetime.now()))

print("setindex:{}".format(datetime.now()))
pd_data.set_index(["company_guid"])
print("endsetindex:{}".format(datetime.now()))

print("1113:{}".format(datetime.now()))
test_data["dic_name"] = test_data.apply(
    lambda row: pd_get(row["company_guid"], pd_data), axis=1)
print("1114:{}".format(datetime.now()))
