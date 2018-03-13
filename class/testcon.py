# coding: utf-8
from concurrent.futures import ProcessPoolExecutor
from concurrent import futures
import time


def count(a, b):
    time.sleep(10)
    print("count {} {}".format(a, b))


def get(m, n):
    time.sleep(5)
    raise Exception("hkh")
    print("get {} {}".format(m, n))


future_result = []
with ProcessPoolExecutor(max_workers=4) as executer:
    future_one = executer.submit(count, 1, 3)
    future_result.append(future_one)
    future_two = executer.submit(get, 1, 3)
    future_result.append(future_two)

for future in futures.as_completed(future_result):
    if future.exception() is not None:
        print('generated an exception: %s' % (future.exception()))
    else:
        print('RunTimes:Res:%s' % (future.result()))

print("finish")

# get(9, 3)
