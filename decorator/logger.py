#!/usr/bin/env python

# logger decorator
from functools import wraps

import datetime
import time

def my_logger(origin_func):
    import logging

    logging.basicConfig(filename='{}.log'.format(origin_func.__name__), level=logging.INFO)

    @wraps(origin_func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] result, args - {}, kwargs - {}'.format(timestamp, args, kwargs))

        return origin_func(*args, **kwargs)

    return wrapper

def my_timer(origin_func):
    import time

    @wraps(origin_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()

        result = origin_func(*args, **kwargs)

        t2 = time.time() - t1

        print('{} func execution time: {} secs'.format(origin_func.__name__, t2))
        return result

    return wrapper

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) func called.'.format(name, age))

display_info('TEST', 26)