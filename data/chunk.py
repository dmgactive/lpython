# coding: utf-8
import pandas as pd
import sqlalchemy

sql_text = "select * from WHODrugDictionary"

source_engine = sqlalchemy.create_engine(
    "mssql+pymssql://EDCAdmin:62451788@192.168.1.207/TM.PV_2_2")
des_engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:Taimei&2017@192.168.1.181/test?charset=utf8")

# mssql_conn = source_engine.connection()
# raise Exception("transaction test")
data_info = pd.read_sql(sql_text, source_engine,chunksize=10000)
for f in data_info:
    f.to_sql("WHODrugDictionary", des_engine, if_exists='append', index=False)
    print("oooooooo")
#print(data_info)
#data_info.to_sql("WHODrugDictionary", des_engine, if_exists='append', index=False)
