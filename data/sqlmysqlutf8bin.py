# coding: utf-8


from sqlalchemy import inspect
import sqlalchemy
import pandas as pd

from sqlalchemy import MetaData
from sqlalchemy import (Enum, ForeignKeyConstraint, PrimaryKeyConstraint, CheckConstraint, UniqueConstraint, Table,
                        Column)

m = 'mysql+mysqlconnector://{}:{}@192.168.1.158:3306/omp?charset=utf8'.format("root", "123456")
# mysql+mysqlconnector://Bi_Airflow:Bi_Airflow@123@172.31.0.211:3310/airflow
# mssql_engine = sqlalchemy.create_engine('mssql+pymssql://sa:Taimei&2017@localhost\dataline/UID')
mysql_engine = sqlalchemy.create_engine(m)
inspector = inspect(mysql_engine)

sql_text = '''select * from t_omp_tenant'''
data = pd.read_sql(sql_text, mysql_engine)
print(data)

m = 'mysql+mysqlconnector://root:123456@192.168.1.139/temp'
engine = sqlalchemy.create_engine(m)

# for table_name in inspector.get_table_names():
#     mysql_columns = []
#     for column in inspector.get_columns(table_name):
#         one_column = Column(column["name"], column["type"])
#         column_type = column["type"]
#         print(column_type)
#         print(str(repr(column_type)))
#         mysql_columns.append(one_column)
# mysql_trans_meta = MetaData()
# mysql_table = Table(table_name, mysql_trans_meta,
#                     *mysql_columns, mysql_engine='InnoDB')
# mysql_table.create(engine)


