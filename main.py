# only find_index is imported
# from my_module import find_index as fi
# path to the module that we want to be found in sys path sys.path.append('......')
import my_module
import sys
courses = ['History', 'Math']
index = my_module.find_index(courses, 'Math')
print(index)
# print(sys.path)

import random
import math
import datetime
import calendar
import os # access to the underlying operating system
random_course = random.choice(courses)
print(random_course)

rads = math.radians(180)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))
# current working directory
print(os.getcwd())