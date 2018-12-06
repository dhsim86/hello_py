#!/usr/bin/env python

from rx import Observable
from rx.testing import marbles

print("---------------------")
print("Marble diagram: a-b-c-|")
xs = Observable.from_marbles("a-b-c-|")
print(xs.to_blocking().to_marbles())

print("---------------------")
print("Marble diagram: (1-2-3-x-5) merge (1-2-3-4-5)")
xs = Observable.from_marbles("1-2-3-x-5")
ys = Observable.from_marbles("1-2-3-4-5")
print(xs.merge(ys).to_blocking().to_marbles())