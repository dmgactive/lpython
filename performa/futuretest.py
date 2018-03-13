# coding: utf-8

from concurrent.futures import ProcessPoolExecutor
from concurrent import futures


def print_df(i):
    print(i)


URLS = ['http://www.xiaorui.cc/',
        'http://blog.xiaorui.cc/',
        'http://ops.xiaorui.cc/',
        'http://www.sohu.com/']

future_result = []

with ProcessPoolExecutor(max_workers=10) as executer:
    future_to_url = dict((executer.submit(print_df, url), url)
                         for url in range(1, 1000))

    for future in futures.as_completed(future_to_url):
        if future.exception() is not None:
            raise Exception(future.exception())
