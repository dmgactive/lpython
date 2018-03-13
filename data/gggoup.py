# coding: utf-8

# coding: utf-8
import pandas as pd
import sqlalchemy
import numpy as np

db_url = 'mysql+mysqlconnector://{0}:{1}@{2}{3}/{4}'.format("root", "123456", "192.168.1.139", ":3306",
                                                            "app_report_perform")
app_engine = sqlalchemy.create_engine(db_url)

sql_text = '''
select company_tm_id, adverse_event_name_soc,count(1) as num
from pv_report
group by company_tm_id,adverse_event_name_soc
'''

# sql_text = "{} group by adverse_event_name_soc".format(sql_text)

# print(sql_text)
data_info = pd.read_sql(sql_text, app_engine)

# print(data_info)
data_info = data_info.dropna()

soc_names = data_info["adverse_event_name_soc"]
soc_names = soc_names.tolist()
print(type(soc_names))

company_ids = data_info["company_tm_id"]
print(type(company_ids))
company_ids = company_ids.tolist()

nums = data_info["num"]

all_data = data_info.groupby(["adverse_event_name_soc"], as_index=False).agg({"num": {'avg': lambda x: np.sum(x)}})
all_data.columns = [col[0] for col in all_data.columns.values]

print(all_data)
