# coding: utf-8
import happybase

connection = happybase.Connection('192.168.1.148', 9090)
print("----------")

table = connection.table('test')#t_omp_tenant

table.put(b'row4', {b'cf:qual1': b'value1',
                       b'cf:qual2': b'value3'})

row = table.row(b'row4')
print(row[b'cf:qual1'])  # prints 'value1'
#
for key, data in table.scan():
    # print(data[b'info:tenant_type'].decode("utf-8") )  # prints row key and data for each row
    print(key, data)

# for key, data in table.scan(row_prefix=b'row'):
#     print(key, data)  # prints 'value1' and 'value2'

# row = table.delete(b'row-key')

# tables=connection.tables()
# print(type(tables))
connection.close()

# catalog = ''.join("""{
#     "table":{"namespace":"default", "name":"t_omp_tenant"},
#     "rowkey":"key",
#     "columns":{
#         "tenant_id":{"cf":"info", "col":"tenant_id", "type":"string"},
#         "tenant_type":{"cf":"info", "col":"tenant_type", "type":"string"},
#         "tenant_name":{"cf":"info", "col":"tenant_name", "type":"string"},
#     }
# }""".split())
#
# print(catalog)
