#!/usr/bin/env python

# Basic
print('--------------------')
print('Basic\n')

f = lambda x: x > 0
g = lambda x: x ** 2

print(list(map(f, range(-5, 5))))
print(list(map(g, range(5))))