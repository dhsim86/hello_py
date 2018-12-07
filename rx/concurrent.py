#!/usr/bin/env python

import multiprocessing
import random
import time
from threading import current_thread

from rx import Observable
from rx.concurrency import ThreadPoolScheduler

core_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(core_count)

def intense_calculation(value):
    time.sleep(random.randint(5, 20) * .1)
    return value

Observable.from_(["Alpha", "Beta", "Gammba", "Delta", "Epsilon"]) \
    .map(lambda s: intense_calculation(s)) \
    .tap(lambda i: print("PROCESS 1 emit: {} {}".format(current_thread().name, i))) \
    .subscribe_on(pool_scheduler) \
    .subscribe(\
        on_next=lambda s: print("PROCESS 1: {} {}".format(current_thread().name, s)),
        on_error=lambda e: print(e),
        on_completed=lambda : print("PROCESS 1: done")
    )

Observable.range(1, 10) \
    .map(lambda s: intense_calculation(s)) \
    .tap(lambda i: print("PROCESS 2 emit: {} {}".format(current_thread().name, i))) \
    .subscribe_on(pool_scheduler) \
    .subscribe(\
        on_next=lambda s: print("PROCESS 2: {} {}".format(current_thread().name, s)),
        on_error=lambda e: print(e),
        on_completed=lambda : print("PROCESS 2: done")
    )

Observable.interval(1000) \
    .map(lambda i: i * 100) \
    .tap(lambda i: print("PROCESS 3 emit: {} {}".format(current_thread().name, i))) \
    .observe_on(pool_scheduler) \
    .map(lambda s: intense_calculation(s)) \
    .subscribe( \
        on_next=lambda s: print("PROCESS 3: {} {}".format(current_thread().name, s)),
        on_error=lambda e: print(e),
        on_completed=lambda: print("PROCESS 3: done")
    )

input("Wait")