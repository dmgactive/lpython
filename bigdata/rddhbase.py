# coding: utf-8
from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("test").master("spark://192.168.1.148:7077").getOrCreate()
hbaseconf = {"hbase.zookeeper.quorum": "192.168.1.148", "hbase.mapreduce.inputtable": "items",
             "hbase.zookeeper.property.clientPort": "2182"}
keyConv = "org.apache.spark.examples.pythonconverters.ImmutableBytesWritableToStringConverter"

valueConv = "org.apache.spark.examples.pythonconverters.HBaseResultToStringConverter"

hbase_rdd = sc.sparkContext.newAPIHadoopRDD( \
    "org.apache.hadoop.hbase.mapreduce.TableInputFormat", \
    "org.apache.hadoop.hbase.io.ImmutableBytesWritable", \
    "org.apache.hadoop.hbase.client.Result", \
    keyConverter=keyConv, valueConverter=valueConv, conf=hbaseconf)
count = hbase_rdd.count()
hbase_rdd.cache()
output = hbase_rdd.collect()
for (k, v) in output:
    print(k, v)
