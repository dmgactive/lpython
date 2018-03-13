# coding: utf-8
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils, TopicAndPartition

sc =SparkSession.builder.appName("test").master("spark://192.168.1.148:7077").getOrCreate()

df = sc \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "192.168.1.148:9092") \
  .option("subscribe", "txt") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")



