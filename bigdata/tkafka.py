# coding: utf-8
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import time


def main():
    ##生产模块
    producer = KafkaProducer(bootstrap_servers=['192.168.1.148:9092'])
    with open('/root/streametl/verify/u.user', 'r') as f:
        for line in f.readlines():
            print(line)
            time.sleep(1)
            # producer.send('txt', line)
            # print(line)
            # producer.flush()


if __name__ == '__main__':
    main()
