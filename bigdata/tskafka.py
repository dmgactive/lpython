# coding: utf-8

from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.streaming import DataStreamWriter

inputPath = "/root/streametl/verify/struct"
spark = SparkSession.builder.appName("test").master("spark://192.168.1.148:7077").config("spark.cores.max",
                                                                                         "1").getOrCreate()
# Since we know the data format already, let's define the schema to speed up processing (no need for Spark to infer schema)
jsonSchema = StructType([StructField("time", TimestampType(), True), StructField("action", StringType(), True)])

# Static DataFrame representing data in the JSON files
# Similar to definition of staticInputDF above, just using `readStream` instead of `read`
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "192.168.1.148:9092") \
    .option("subscribe", "clinic") \
    .option("startingOffsets", "earliest")\
    .load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")


# df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
#   .write \
#   .format("kafka") \
#   .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
#   .option("topic", "topic1") \
#   .save()

query = (
    df
    .writeStream
    .format("jdbc")    # counts = name of the in-memory table
    .outputMode("append")  # complete = all the counts should be in the table
    .start()
)

query.awaitTermination()
