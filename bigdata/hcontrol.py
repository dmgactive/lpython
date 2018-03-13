# coding: utf-8

import happybase

connection = happybase.Connection(host='192.168.1.148',port=9090)
connection.create_table(
    'ccc',
    {'rowkey': dict(max_versions=10),
     'info': dict(max_versions=1, block_cache_enabled=False),
    }
)


