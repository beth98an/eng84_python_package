# Python packages

from random import random # generates random numbers
import math

print(random())

num_float = 23.6
print("actual float value " + str(num_float))
print(math.ceil(num_float))  # ceil() rounds up the value
print(math.floor(num_float))  # floor() rounds down the value

# Python Modules

import os
import datetime, sys

working_directory = os.getcwd() # it tells us the current directory location
print(working_directory)

# print(os.uname()) does not work on windows
print(os.cpu_count())
print(datetime.date.today())
print(sys.path)
print(math.pi)