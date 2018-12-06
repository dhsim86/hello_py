#!/usr/bin/env python

from rx import Observable, Observer

def push_hello_world(observer):
    observer.on_next("hello")
    observer.on_next("world")
    observer.on_completed()

class PrintObserver(Observer):
    def on_next(self, value):
        print("{}.onNext: {}".format(self.__class__.__name__, value))

    def on_completed(self):
        print("{}.onComplete".format(self.__class__.__name__))

    def on_error(self, error):
        print("{}.onError: {}".format(self.__class__.__name__, error))

class ListObserver(Observer):
    def __init__(self):
        self.my_list = []

    def on_next(self, value):
        print("{}.onNext: {}".format(self.__class__.__name__, value))
        self.my_list.append(value)

    def on_completed(self):
        print("{}.onComplete: {}".format(self.__class__.__name__, self.my_list))

    def on_error(self, error):
        print("{}.onError: {}".format(self.__class__.__name__, error))

if __name__ == '__main__':
    source = Observable.create(push_hello_world)
    source.subscribe(PrintObserver())
    source.subscribe(ListObserver())

