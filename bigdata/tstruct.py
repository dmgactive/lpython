# coding: utf-8
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

inputPath = "/root/streametl/verify/struct"
spark = SparkSession.builder.appName("test").master("spark://192.168.1.148:7077").config("spark.cores.max", "1").getOrCreate()
# Since we know the data format already, let's define the schema to speed up processing (no need for Spark to infer schema)
jsonSchema = StructType([StructField("time", TimestampType(), True), StructField("action", StringType(), True)])

# Static DataFrame representing data in the JSON files
# Similar to definition of staticInputDF above, just using `readStream` instead of `read`
streamingInputDF = (
  spark
    .readStream
    .schema(jsonSchema)               # Set the schema of the JSON data
    .option("maxFilesPerTrigger", 1)  # Treat a sequence of files as a stream by picking one file at a time
    .json(inputPath)
)

# Same query as staticInputDF
streamingCountsDF = (
  streamingInputDF
    .groupBy(
      streamingInputDF.action,
      window(streamingInputDF.time, "1 hour"))
    .count()
)

spark.conf.set("spark.sql.shuffle.partitions", "2")  # keep the size of shuffles small

query = (
  streamingCountsDF
    .writeStream
    .format("console")        # memory = store in-memory table (for testing only in Spark 2.0)
    .queryName("counts")     # counts = name of the in-memory table
    .outputMode("complete")  # complete = all the counts should be in the table
    .start()
)

query.awaitTermination()