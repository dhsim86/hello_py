#!/usr/bin/env python

# Default Variable Example
def menu(wine, entree, dessert = 'pudding'):
  return { 'wine': wine, 'entree' : entree, 'dessert' : dessert}

#print(menu('chardonnay', 'chicken', 'cake'))
#print(menu(entree = 'beef', dessert = 'bagel', wine = 'boardeaux'))
#print(menu('frontenac', dessert = 'flan', entree = 'fish'))
#print(menu('chardonnay', 'chicken'))

########################################################################

# Default variable is calculated when function defintion.
def buggy(arg, result = []):
  result.append(arg)
  print(result)

def nonbuggy(arg, result = None):
  if result is None:
    result = []
  result.append(arg)
  print(result)

#buggy('a')
#buggy('b')

#nonbuggy('a')
#nonbuggy('b')

########################################################################

# * represents tuple.
def print_args(*args):
  print('Positional argument tuple:', args)

def print_more(required1, required2, *args):
  print('required parameter: ', required1, required2)
  print('all rest args: ', args)

#print_args()
#print_args(3, 2, 1, 'wait!', 'uh...')

#print_more(1, 2)
#print_more(1, 2, 3)
#print_more(1, 2, 3, 4)

########################################################################

# ** represents dictionary.
def print_kwargs(**kwargs):
  print('Keyword arguments:', kwargs)

#print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

########################################################################

# function help.
def echo(anyting):
  'echo returns its input argument'
  return anyting

def print_if_true(thing, check):
  '''
  Prints the first argument if a second argument is true.
  The operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
  '''

  if check:
    print(thing)

#print(echo.__doc__)

########################################################################

# function is object
def answer():
  print(42)

def run_something(func):
  func()

def add_args(arg1, arg2):
  print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
  func(arg1, arg2)

#run_something(answer)
#run_something_with_args(add_args, 5, 9)

########################################################################

# function is object
def sum_args(*args):
  return sum(args)

def run_with_positional_args(func, *args):
  return func(*args)

#print(run_with_positional_args(sum_args, 1, 2, 3, 4))

########################################################################

# We can define inner function.
def outer(a, b):
  def inner(c, d):
    return c + d
  return inner(a, b)

#print(outer(4, 7))

########################################################################

# Closure example
def knight(saying):
  def inner():
    return "We are the knights who say: '%s'" % saying
  return inner

a = knight('Duck')
b = knight('Haspenfeffer')

#print(a())
#print(b())

########################################################################

# Lambda

def edit_story(words, func):
  for word in words:
    print(func(word))

def enliven(word):
  return word.capitalize() + '!'

stairs = ['thud', 'meow', 'thud', 'hiss']

#edit_story(stairs, enliven)
#edit_story(stairs, lambda word: word.capitalize() + '!')

########################################################################

# Generator

def my_range(first = 0, last = 10, step = 1):
  number = first
  while number < last:
    yield number
    number += step

ranger = my_range(1, 5)
#for x in ranger:
  #print(x)

########################################################################

# Decorator

def document_it(func):
  def new_function(*args, **kwargs):
    print('Running function: ', func.__name__)
    print('Positional arguments: ', args)
    print('Keyword arguemnts: ', kwargs)
    result = func(*args, **kwargs)
    print('Result: ', result)
    return result
  return new_function

def square_it(func):
  def new_function(*args, **kwargs):
    result = func(*args, **kwargs)
    return result * result
  return new_function

def add_ints(a, b):
  return a + b

@document_it
def add_ints2(a, b):
  return a + b

@document_it
@square_it
def add_ints3(a, b):
  return a + b

#print(add_ints(3, 5))
#cooler_add_ints = document_it(add_ints)
#cooler_add_ints(3, 5)
#print(add_ints2(3, 5))
print(add_ints3(3, 5))

########################################################################

# exception

def except_test(idx):
  short_list = [1, 2, 3]
  try:
    short_list[idx]
  except:
    print('Need a position between 0 and', len(short_list) - 1, ' bug got', idx)

#except_test(5)

########################################################################

class UppercaseException(Exception):
  pass

words = ['eeenie', 'meenie', 'miny', 'MO']
#for word in words:
  #if word.isupper():
    #raise UppercaseException(word)

class OopsException(Exception):
  pass

try:
  raise OopsException('panic')
except OopsException as exc:
  print(exc)
########################################################################
