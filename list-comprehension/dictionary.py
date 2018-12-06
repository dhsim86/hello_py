#!/usr/bin/env python

text = 'cheese'

D = {i: text.count(i) for i in text}
print(D)