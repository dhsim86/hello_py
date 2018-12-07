#!/usr/bin/env python

from rx import Observable

print("---------------------")
print("combine observable")

letters = Observable.from_(['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']) \
    .tap(lambda s: print("letter observable emit: {}".format(s)))

intervals = Observable.interval(1000) \
    .tap(lambda i: print("interval observable emit: {}".format(i)))

Observable.zip(letters, intervals, lambda s, i: (s, i)) \
    .subscribe(lambda t: print("zip subscribe: {}".format(t)))

input("Wait\n")