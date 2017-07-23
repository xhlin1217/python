# Modules and Packages
import prime
print(dir(prime))	# function can be found in prime
print(prime.primesTo(100))

# same as following
import prime as p
print(p.primesTo(100))

# import just the function from the modules
from prime import primesTo
primesTo(10)

import main.sub.prime as p
print(p.primesTo(100))

from main.sub.prime import primesTo
print(primesTo(100))


# Buildin Modules
import copy
myDictionary = {'key': 'Value'}
yourDictionary = copy.deepcopy(myDictionary)
print(myDictionary)
print(yourDictionary)
myDictionary['newKey'] = 'newValue'
print(myDictionary)
print(yourDictionary)

import math
print(math.ceil(1.6))
print(math.floor(1.6))

import random as ran
print(ran.random())
print(ran.randint(1, 100))


import sys
print(sys.version)	# python version
print(sys.path)
