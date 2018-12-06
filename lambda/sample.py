#!/usr/bin/env python

# Basic
print('--------------------')
print('Basic\n')

f = lambda x, y: x + y
print(f(1, 2))
print(f([1, 2], [3, 4]))
print(f("TEST", "SET"))

# Default
print('--------------------')
print('Default\n')

f2 = lambda x, y = 3: x + y
print(f2(1))
print(f2(3, 3))

# Multiple Parameter
print('--------------------')
print('Multiple Parameter\n')

f3 = lambda *x: max(x) * 2
print(f3(1, 3, 7))