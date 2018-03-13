# coding: utf-8
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession

# sc = SparkContext()
# sqlc = SQLContext(sc)
sc = SparkSession.builder.appName("test").master("spark://192.168.1.148:7077").getOrCreate()
ctx = SQLContext(sc)
data_source_format = 'org.apache.spark.sql.execution.datasources.hbase'
catalog = ''.join("""{
    "table":{"namespace":"default", "name":"ccc"},
    "rowkey":"a",
    "columns":{
        "id":{"cf":"rowkey", "col":"a", "type":"string"},
        "firstcol":{"cf":"info", "col":"b", "type":"string"}
    }
}""".split())
df = sc.read \
    .options(catalog=catalog) \
    .format(data_source_format) \
    .load()
df.show()


