#!/usr/bin/env python

import sys
import report

# standalone
# print('Program arguments:', sys.argv)

########################################################################

# description = report.get_description()
# print("Today's weather:", description)

########################################################################

# from sources import daily, weekly

# print("Daily forecast:", daily.forecast())
# print("Weekly forecast:", weekly.forecast())

# for number, outlook in enumerate(weekly.forecast(), 1):
  #print(number, outlook)

########################################################################

# periodic_table = {'Hydrogen': 1, 'Helium': 2}
# print(periodic_table)

# carbon = periodic_table.setdefault('Carbon', 12)
# print(carbon)
# print(periodic_table)

# helium = periodic_table.setdefault('Helium', 947)
# print(helium)
# print(periodic_table)

########################################################################

# from collections import defaultdict
# periodic_table = defaultdict(int)
# print(periodic_table)

# periodic_table['Hydrogen'] = 1
# periodic_table['Lead']

# print(periodic_table)

########################################################################

# from collections import defaultdict

# def no_idea():
#   return 'Huh?'

# bestiary = defaultdict(no_idea)
# bestiary['A'] = 'Abominable Snowman'
# bestiary['B'] = 'Basilisk'
# bestiary['C']

# print(bestiary)

########################################################################

# from collections import defaultdict

# bestiary = defaultdict(lambda: 'Huh?')
# print(bestiary['E'])

# food_counter = defaultdict(int)
# for food in ['spam', 'spam', 'eggs', 'spam']:
#  food_counter[food] += 1

# for food, count in food_counter.items():
#  print(food, count)

########################################################################

# from collections import Counter

# breakfast = ['spam', 'spam', 'eggs', 'spam']
# breakfast_counter = Counter(breakfast)
# print(breakfast_counter)

########################################################################

quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk, nyuk!',
  }
for stooge in quotes:
  print(stooge)

########################################################################

from collections import OrderedDict
orderedQuotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk, nyuk!'),
  ])

for stooge in orderedQuotes:
  print(stooge)