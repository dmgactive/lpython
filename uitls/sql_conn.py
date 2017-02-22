# coding: utf-8

import pymssql
import sqlalchemy

# 密码中包含特殊字符
conn = pymssql.connect(host='localhost\dataline', user='tim', password='taimei@2017', database='UID')

from urllib.parse import quote_plus as urlquote

m='mssql+pymssql://{}:{}@localhost\dataline/UID'.format("tim",urlquote("taimei@2017"))
print(m)

# mssql_engine = sqlalchemy.create_engine('mssql+pymssql://sa:Taimei&2017@localhost\dataline/UID')
mssql_engine = sqlalchemy.create_engine(m)
mssql_engine.execute("  ")

