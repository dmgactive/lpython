# coding: utf-8
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils, TopicAndPartition


def start():
    # sc = SparkContext(appName='txt', conf=sconf)
    sc = SparkContext("spark://192.168.1.148:7077", "NetworkWordCount")
    ssc = StreamingContext(sc, 3)
    brokers = "192.168.1.148:2181"
    topic = 'clinic'

    user_data = KafkaUtils.createStream(ssc, brokers, "spark-streaming-consumer", {topic: 1})
    # fromOffsets 设置从起始偏移量消费
    # user_data = KafkaUtils.createDirectStream(ssc,[topic],kafkaParams={"metadata.broker.list":brokers},fromOffsets={TopicAndPartition(topic,partition):long(start)})
    user_data.pprint()
    ssc.start()
    ssc.awaitTermination()


offsetRanges = []


def offset(rdd):
    global offsetRanges
    offsetRanges = rdd.offsetRanges()


def echo(rdd):
    zhiye = rdd[0]
    num = rdd[1]
    for o in offsetRanges:
        topic = o.topic
        partition = o.partition
        fromoffset = o.fromOffset
        untiloffset = o.untilOffset
        # 结果插入MySQL
        print("------22222222---")
    # conn = MySQLdb.connect(user="root", passwd="******", host="192.168.26.245", db="test", charset="utf8")
    # cursor = conn.cursor()
    # sql = "insert into zhiye(id,zhiye,num,topic,partitions,fromoffset,untiloffset) \
    # values (NULL,'%s','%d','%s','%d','%d','%d')" % (zhiye, num, topic, partition, fromoffset, untiloffset)
    #
    #
    # cursor.execute(sql)
    # conn.commit()
    # conn.close()
    # connection = pymysql.connect(host='192.168.1.148',
    #                              user='root',
    #                              password='123456',
    #                              db='db',
    #                              charset='utf8mb4',
    #                              cursorclass=pymysql.cursors.DictCursor)
    #
    # try:
    #     with connection.cursor() as cursor:
    #         # Create a new record
    #         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    #     # connection is not autocommit by default. So you must commit to save
    #     # your changes.
    #     connection.commit()
    #
    #     with connection.cursor() as cursor:
    #         # Read a single record
    #         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #         cursor.execute(sql, ('webmaster@python.org',))
    #         result = cursor.fetchone()
    #         print(result)
    # finally:
    #     connection.close()


if __name__ == '__main__':
    start()
