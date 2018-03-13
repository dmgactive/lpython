# coding: utf-8
import uuid
from datetime import datetime
import timeit
import pandas as pd
import sqlalchemy

db_url = 'mysql+mysqlconnector://{0}:{1}@{2}{3}/{4}'.format("root", "123456", "192.168.1.139", ":3306",
                                                            "dw_go")
app_engine = sqlalchemy.create_engine(db_url)

for i in range(0, 30):
    print(i)
    tms_data = pd.DataFrame(
        {'employee_id': [uuid.uuid1().int >> 64 for i in range(0, 1000000)]
         }
    )
    tms_data.to_sql('uid_int', app_engine, if_exists='append', index=False, chunksize=10000)

app_engine = sqlalchemy.create_engine(db_url)

# for i in range(0, 20):
#     print(i)
#     tms_data = pd.DataFrame(
#         {'employee_id': [str(uuid.uuid1()) for i in range(0, 1000000)]
#          }
#     )
#     tms_data.to_sql('uid_string', app_engine, if_exists='append', index=False, chunksize=10000)
