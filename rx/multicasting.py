#!/usr/bin/env python

from rx import Observable
from random import randint

print("---------------------")
print("cold observable")

cold = Observable.range(1, 3) \
    .map(lambda i: randint(1, 100000)) \
    .tap(lambda i: print("Emit {}".format(i)))

cold.subscribe(lambda i: print("Subscriber 1 Received: {}".format(i)))
cold.subscribe(lambda i: print("Subscriber 2 Received: {}".format(i)))

print("---------------------")
print("hot observable #0: connect() invoke")

hot = Observable.range(1, 3) \
    .map(lambda i: randint(1, 100000)) \
    .tap(lambda i: print("Emit {}".format(i))) \
    .publish()

hot.subscribe(lambda i: print("Subscriber 1 Received: {}".format(i)))
hot.subscribe(lambda i: print("Subscriber 2 Received: {}".format(i)))

hot.connect()

print("---------------------")
print("hot observable #1: without connect()")

hot = Observable.range(1, 3) \
    .map(lambda i: randint(1, 100000)) \
    .tap(lambda i: print("Emit {}".format(i))) \
    .publish() \
    .auto_connect(2)

hot.subscribe(lambda i: print("Subscriber 1 Received: {}".format(i)))
hot.subscribe(lambda i: print("Subscriber 2 Received: {}".format(i)))




