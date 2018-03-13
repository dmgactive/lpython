# coding: utf-8
import pandas as pd
from datetime import datetime
import numpy as np

left_data = pd.DataFrame(
    {'A': [2, 3, 4, 5],
     'B': [5, 6, 7, 9],
     'C': [8, 12, 0, 3]
     }
)

right_data = pd.DataFrame(
    {'A': [2, 3],
     'M': [5, 6],
     'B': [3, 2],
     'N': [8, 12]
     }
)

# right_data = pd.DataFrame(
#     {'A': [2, 3]
#      }
# )

merge_data = pd.merge(left_data, right_data, left_on=["A"], right_on=["A"], how="left", suffixes=["", "_y"],
                      indicator=True)

print(merge_data)

merge_data = merge_data[merge_data["M"].isnull()].drop("M", 1)

print(merge_data)

# sat update

left_data = pd.DataFrame(
    {'id': [2, 3, 4, 5],
     'B': [5, 6, 7, 9],
     'C': [8, 12, 0, 3],
     'hashdiff': [5, 4, 3, 2]
     }
)

right_data = pd.DataFrame(
    {'A': [2, 3],
     'B': [5, 6],
     'C': [8, 7],
     'hashdiff': [5, 3]
     }
)
m = datetime.now()
print(str(m))
# not same insert
# same

#
basic_info = pd.DataFrame({
    "PIT": ["PID1", "PID2", "PID3"],
    "LN": ["LN1", "LN2", "LN3"],
    "field": ["name", "name", "name"],
    "reportid": [1, 2, 3],
    "itemid": ["1", "2", "3"]
})

adverse_info = pd.DataFrame({
    "reportid": [1, 2, 3, 4],
    "name": ["1", "2", "3", "4"]
})

code_columns = ["PIT", "LN"]

print(basic_info[(basic_info["field"] == "name") & (basic_info["reportid"] == 2) & (basic_info["itemid"] == "2")][
          ["PIT", "LN"]])


def get_basic(reportid, item_id):
    value = basic_info[
        (basic_info["field"] == "name") & (basic_info["reportid"] == reportid) & (basic_info["itemid"] == item_id)][
        ["PIT", "LN"]]
    if (len(value)) > 0:
        return value.iloc[0]
    else:
        return pd.Series()


adverse_info[["PIT", "LN"]] = adverse_info.apply(lambda row: get_basic(row["reportid"], row["name"]), axis=1)

print(adverse_info)

# drop duplicate
dup_info = pd.DataFrame(
    {
        'A': [12, 10, 1, 9, 9, 9, 20, 12],
        'B': [30, 1, 3, 2, 60, 7, 20, 1],
        'C': [1, 3, 5, 6, 7, 0, 9, 1]
    }
)

print(dup_info)
print("-------------------")
print(dup_info.groupby('A', group_keys=False).apply(lambda x: x.ix[x.B.idxmax()]))
print("&&&&&&&&&&&&&&&&&&&&&")
# print(dup_info.groupby(['A']).max(['B']))
print("*************")
ss = dup_info.sort_values(['A', 'B'], ascending=[True, True])
ss = ss.drop_duplicates(['A'], keep='last')
print(ss)
print("$$$$$$$$$$$$$$$$$")
dup_info = dup_info.drop_duplicates(['A'], keep='last')
print("****************")
print(dup_info)

dup_info = pd.DataFrame(
    {
        'A': [12, 10, 1, 9, 9, 9, 20, 12],
        'B': [30, 1, 3, 2, 60, 7, 20, 1],
        'C': [1, 3, 5, 6, 7, 0, 9, 1]
    }
)
dup_info["max_value"] = dup_info.groupby(['A'])['B'].transform(max)
print(len(dup_info))
# dup_info["max_label"] = dup_info.apply(lambda row: 'true' if row["A"] == row['B'] else 'false')

# dup_info["max_label"] = dup_info.groupby("A")['B'].transform(lambda x: 'true' if x["B"] > 0 else 'false')
# dup_info["m"] = dup_info.groupby("A").transform(lambda x: (x - x.mean()) / x.std())
# dup_info["max_label"] = dup_info.groupby("A")['B'].(lambda x: 'true' if x["B"] > 0 else 'false')
