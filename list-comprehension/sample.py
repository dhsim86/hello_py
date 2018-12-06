#!/usr/bin/env python

# All

L = [i ** 2 for i in range(10)]
print(L)

# Condition

L1 = [i ** 2 for i in range(10) if (i > 5)]
print(L1)

L2 = [i ** 2 for i in range(10) if (i > 5) and (i % 2 == 0)]
print(L2)