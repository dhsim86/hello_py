#!/usr/bin/env python

# Basic
print('--------------------')
print('Basic\n')

f = lambda x: x > 0
print(list(filter(f, range(-5, 5))))

