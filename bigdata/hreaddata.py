# coding: utf-8
import happybase

connection = happybase.Connection(host='192.168.1.148',port=9090)
print("----------")
# print(connection.tables())
table = connection.table('items')#t_omp_tenant
print(table)
#
# table.put(b'row4', {b'cf:qual1': b'value1',
#                        b'cf:qual2': b'value3'})
#
# row = table.row(b'row4')
# print(row[b'cf:qual1'])  # prints 'value1'

for key, data in table.scan():
    print(key, data)
    print(type(data[b'info:Name_chs'].decode("utf-8")))
    print(type(data[b'info:CompanyId'].decode("utf-8")))
    print(data[b'info:CompanyId'])
    print(data[b'info:CompanyId'].decode("utf-8"))
    print(data[b'info:Name_chs'].decode("utf-8") )  # prints row key and data for each row
    print(key, data)

# for key, data in table.scan(row_prefix=b'row'):
    # print(key, data)  # prints 'value1' and 'value2'

# row = table.delete(b'row-key')

# tables=connection.tables()
# print(type(tables))
# connection.close()

# schema = StructType([StructField("name", StringType(), True),StructField("age", IntegerType(), True)])



