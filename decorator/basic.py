#!/usr/bin/env python

# Basic
print('--------------------')
print('Basic\n')

def decorator_func(origin_func):
    def wrap_func():
        return origin_func()

    return wrap_func

def display():
    print('Called display func')

dis = decorator_func(display)
dis()

# logger
del decorator_func
del display

print('--------------------')
print('logger\n')

def decorator_func(origin_func):
    def wrapper():
        print('{} func call before.'.format(origin_func.__name__))
        return origin_func()
    return wrapper

def display1():
    print('display1 called.')

def display2():
    print('display2 called.')

display_1 = decorator_func(display1)
display_2 = decorator_func(display2)

display_1()
print('\n')
display_2()