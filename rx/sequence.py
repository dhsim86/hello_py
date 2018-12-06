#!/usr/bin/env python

from rx import Observable, Observer

class MyObserver(Observer):
    def on_next(self, x):
        print("{}.onNext: {}".format(self.__class__.__name__, x))

    def on_completed(self):
        print("{}.onComplete".format(self.__class__.__name__))

    def on_error(self, error):
        print("{}.onError: {}".format(self.__class__.__name__, error))

xs = Observable.from_iterable(range(10))

print("---------------------")
print("MyObserver subscribe")
d = xs.subscribe(MyObserver())

print("---------------------")
print("print subscribe")
d = xs.subscribe(print)

print("---------------------")
print("filter x % 2")
d = xs.filter(lambda x: x % 2).subscribe(print)

print("---------------------")
print("map x * 2")
d = xs.map(lambda x: x * 2).subscribe(print)

print("---------------------")
print("generator map {index}: {x * 2}")
xs = Observable.from_(range(10, 20, 2))
d = xs.map(lambda x, i: "%s: %s" % (i, x * 2)).subscribe(print)

print("---------------------")
print("merge (zip) {index}: {x * 2}")
xs = Observable.range(1, 5)
ys = Observable.from_("abcde")
zs = xs.merge(ys).subscribe(print)

