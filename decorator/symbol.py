#!/usr/bin/env python

print('--------------------')
print('symbol\n')

def decorator_func(origin_func):
    def wrapper():
        print('{} func call before'.format(origin_func.__name__))
        return origin_func()
    return wrapper

@decorator_func
def display_1():
    print('display1 called.')

@decorator_func
def display_2():
    print('display2 called.')

display_1()
display_2()

# parameter

del decorator_func
del display_1
del display_2

print('--------------------')
print('parameter\n')

def decorator_func(origin_func):
    def wrapper(*args, **kwargs):
        print('{} func call before'.format(origin_func.__name__))
        return origin_func(*args, **kwargs)

    return wrapper

@decorator_func
def display():
    print('display func called')

@decorator_func
def display_info(name, age):
    print('display_info({}, {}) func called'.format(name, age))

display()
print
display_info('test', 25)

# decorator class

del decorator_func
del display
del display_info

print('--------------------')
print('decorator class\n')

class DecoratorClass:
    def __init__(self, origin_func):
        self.origin_func = origin_func

    def __call__(self, *args, **kwargs):
        print('{} func call before'.format(self.origin_func.__name__))
        return self.origin_func(*args, **kwargs)

@DecoratorClass
def display():
    print('display func called')

@DecoratorClass
def display_info(name, age):
    print('display_info({}, {}) func called.'.format(name, age))

display()
print
display_info('TEST_SET', 26)