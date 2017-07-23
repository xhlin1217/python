# tuple ==> ()
# cannot change once it assign
tup = (1,2,3)
print(tup)	# (1, 2, 3)
tup = tup + (111,) # adding element into tup
print(tup)	# (1, 2, 3, 111)

tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efg', True
tup2 = 'A' # same as tup2 = ('A',)
print(tup)
print(tup1)
print(tup2)

tup = 9,4,2,33,1
print(tup[1])	# accessing tuple
print(tup[1:2])	# return tup element, starting in 1 index, and stop in 2 index
print(tup[1])
# tup[1] = 'hello'	# this will cause an error

# 'tuple' object does not support item assignment
try:
	tup[1] = 'hello'
except Exception as e:
	print(e)	

print('first' in tup)	# checking if 'first' is in tupe

# tuple in loop
for i in tup:
	print(i)

# tuple function
print(len(tup))	# return the size of the tuple
print(max(tup))	# return the max element of the tuple
print(min(tup))	# return the min element of the tuple

# list
list1 = [1, 'second', (3, 4)]
print(list1)		# print list
print(list1[2])		# access element in list
print(1 in list1)	# checking is 1 in list1
print(list1)
list1.append('last')# adding element to list
print(list1)
print(len(list1))	# return the lenth of the list


# List Function
listForFunction = [1,2,3,4]
print(list(map(lambda x: x ** 2, listForFunction)))		# x^2
print(list(filter(lambda x: x > 2, listForFunction)))	# filter all element that is > 2
import functools
print(functools.reduce(lambda x, y : x * y, listForFunction))	# 1 * 2 * 3 * 4 = 24


# dictionary, key value pair
dictionary = {1 : 'one', 'list' : [1,2,3]}
print(dictionary)	# print dictionary
print(dictionary.keys())	# print all the keys in dictionary
print(dictionary.values())	# print all the values in dictionary
print(dictionary)
dictionary['newkey'] = 'newValue'	# adding new element in dictionary
print(dictionary)
dictionary.clear()	# clear all element in dictionary
print(dictionary)

# Shallow Copies with Dictionaries
# shallow copy: two copies of a data structure share the same set of elements
myDictionary = {1: 'one', 2: 'two', 3: 'three'}
myDictionary1 = myDictionary
print(myDictionary)
print(myDictionary1)
myDictionary[1] = 'first'	# share same location address
print(myDictionary)
print(myDictionary1)


# # Set - no repeat value in set (hash Set), | ^ -
mySet = set(['one', 'two', 'three'])
yourSet = set(['two', 'three', 'four'])
anotheSet = set(['one'])
print(mySet | yourSet)	# union, {'three', 'two', 'one', 'four'}
print(mySet ^ yourSet)	# unique of both set, {'one', 'four'}
print(mySet - yourSet)	# element only exist in myset, {'one'}
print(anotheSet <= mySet)	# anotherSet is the subset of mySet, true
print(mySet)
mySet.add('five')	# adding element to mySet
print(mySet)

# Set functions
print(set.union(mySet, yourSet))		# {'one', 'two', 'three', 'four'}
print(set.intersection(mySet, yourSet))	# {'two', 'three'}
print(set.difference(mySet, yourSet))	# {'one'}