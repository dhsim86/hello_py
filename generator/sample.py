#!/usr/bin/env python

from __future__ import division
import psutil
import os
import random
import time

names = ['TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5', 'TEST6']
majors = ['MAJOR1', 'MAJOR2', 'MAJOR3', 'MAJOR4', 'MAJOR5']

process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024

def people_list(num_people):
    result = []

    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

mem_after = process.memory_info().rss / 1024 / 1024
total_time = t2 - t1

print('Previous memory: {} MB'.format(mem_before))
print('After memory: {} MB'.format(mem_after))
print('Total time: {:.6f} sec'.format(total_time))