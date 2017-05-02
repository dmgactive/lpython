# coding: utf-8
import pandas as pd
from datetime import datetime

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

merge_data = pd.merge(left_data, right_data, left_on=["A"], right_on=["A"], how="left", suffixes=["","_y"],indicator=True)

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
