# coding: utf-8

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext

sc = SparkSession.builder.appName("test").master("spark://192.168.1.148:7077").getOrCreate()
ctx = SQLContext(sc)
jdbcDf = ctx.read.format("jdbc").options(url="jdbc:mysql://192.168.1.139:3306/app_report",
                                         driver="com.mysql.jdbc.Driver",
                                         dbtable="(SELECT * FROM pv_report) tmp", user="root",
                                         password="123456").load()
jdbcDf.count()
