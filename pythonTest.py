def variables():
	a = 1
	b = a + 1
	print(a)
	print("this is a new value for b: " + str(b))
	print("a = {}, and b = {}".format(a, b))
# variables()
# # 1
# # this is a new value for b: 2
# # a = 1, and b = 2

def conditional():
	this_boolean = False
	if this_boolean:
		print("this_boolean is true")
	if this_boolean == False:
		print("this_boolean is false")

	number = 0
	if(number == 1):
		print("number = 1")
	elif(number == 2):
		print("number = 2")
	else:
		print("number either less than 1 or greater than 2")

	store = "good foods"
	if "auto" in store:
		print("this is a auto store")
	elif "food" in store:
		print("this is a food store")
	else:
		print("the store is for something else")
# conditional()
# # this_boolean is false
# # number either less than 1 or greater than 2
# # this is a food store

def list_and_dictionaries():
	itemArray = ["apple", "orange"]
	print(itemArray)
	print(str(len(itemArray)) + " items are in itemArray")
	print("the first element in itemArray: " + str(itemArray[0]))
	itemArray.append("banana")
	print("adding item to itemArray: " + str(itemArray))
	itemArray[0] = "new apple"
	print("update itemArray element: " + str(itemArray))
	itemArray.remove("orange")
	print("remove item from itemArray: " + str(itemArray), end="\n\n")

	dictionaries = {"apple" : 10, "banana" : 20, "orange" : 30}
	print(dictionaries)
	print("there are " + str(len(dictionaries)) + " items in dictionaries")
	print("the value for apple is: " + str(dictionaries["apple"]))
	print("getting all the keys in dictionaries" + str(dictionaries.keys()))
	print("getting all the values in dictionaries" + str(dictionaries.values()))
	# remove item from dictionary
	popItemValue = dictionaries.pop("apple")
	print("popItemValue: " + str(popItemValue) + ", dictionaries: " + str(dictionaries))
	# add item to dictionary
	dictionaries["cherries"] = 26
	print(dictionaries)
# list_and_dictionaries()
# # ['apple', 'orange']
# # 2 items are in itemArray
# # the first element in itemArray: apple
# # adding item to itemArray: ['apple', 'orange', 'banana']
# # update itemArray element: ['new apple', 'orange', 'banana']
# # remove item from itemArray: ['new apple', 'banana']

# # {'apple': 10, 'banana': 20, 'orange': 30}
# # there are 3 items in dictionaries
# # the value for apple is: 10
# # getting all the keys in dictionariesdict_keys(['apple', 'banana', 'orange'])
# # getting all the values in dictionariesdict_values([10, 20, 30])
# # popItemValue: 10, dictionaries: {'banana': 20, 'orange': 30}
# # {'banana': 20, 'cherries': 26, 'orange': 30}


# loops
def whileLoop():
	apple = 10
	banana = 20
	grapes = 30

	items = [apple, banana, grapes]
	index = 0
	while index < len(items):
		print(items[index])
		index += 1
	else:
		print("no more item in items, index = " + str(index))
# whileLoop()
# # 10
# # 20
# # 30
# # no more item in items, index = 3

def forloop():
	items = ["apple", "banana", "grapes"]
	itemsDictionary = {'apple' : 10, 'banana' : 20, 'orange': 30}
	print("item in items: ")
	for item in items:
		print("\t" + item, end=" ")
	print("\nitem in itemsDictionary: ")
	for item in itemsDictionary:
		print("\t" + item, end = " ")
	print("\nkey value pair item in itemsDictionary: ")
	for k,v in itemsDictionary.items():
		print("\tkey: " + k + ", value: " + str(v))
	print("\nkey item in itemsDictionary: ")
	for k in itemsDictionary.keys():
		print("\t" + k, end = " ")
	print("\nvalue item in itemsDictionary: ")
	for v in itemsDictionary.values():
		print("\t" + str(v), end = " ")
	print()

# forloop()
# # item in items: 
# # 	apple 	banana 	grapes 
# # item in itemsDictionary: 
# # 	banana 	apple 	orange 
# # key value pair item in itemsDictionary: 
# # 	key: banana, value: 20
# # 	key: apple, value: 10
# # 	key: orange, value: 30

# # key item in itemsDictionary: 
# # 	banana 	apple 	orange 
# # value item in itemsDictionary: 
# # 	20 	10 	30 


def string():
	# format string into dictionary
	long_string = "apple-10|bananas-15 | grapes-19 | cherries-14"
	item = {}
	new_str = long_string.replace(" ", "")
	print('long_string: ' + long_string)
	print('new_str: ' + new_str)
	new_str = new_str.split("|")
	print(new_str)
	for i in new_str:
		a, b = i.split('-')
		print('\t' + a + " - " + b)
		item[a] = b
	print(item)
	print(item.keys())
	print(item.values())

# string()
# # long_string: apple-10|bananas-15 | grapes-19 | cherries-14
# # new_str: apple-10|bananas-15|grapes-19|cherries-14
# # ['apple-10', 'bananas-15', 'grapes-19', 'cherries-14']
# # 	apple - 10
# # 	bananas - 15
# # 	grapes - 19
# # 	cherries - 14
# # {'bananas': '15', 'grapes': '19', 'cherries': '14', 'apple': '10'}
# # dict_keys(['bananas', 'grapes', 'cherries', 'apple'])
# # dict_values(['15', '19', '14', '10'])


# tuples return mutil variables
def tuples():
	apple = 'apple'
	appleQty = 10
	anItem = apple + ':' + str(appleQty)

	print(anItem)
	a, b = anItem.split(':')
	print(a)
	print(b)
	tuples = anItem.split(':')
	print(tuples[1])

	inventory = {"apple":10, "banana":15, 'orange':20}
	for k,v in inventory.items():
		print('\t' + k + ', Qty = ' + str(v))

	# create tuples
	items = (1, )
	print("first and only item in items: " + str(items[0]))
	items = ('first', 'second', 'third', 'fourth')
	print(items[1 : 4])

	numbers = (1,2,3,4,5)
	print(numbers[1:4])
	print(numbers[0])
	# cannot overwrite
	# numbers[0] = 2
	numbers = (22,33,44,55)
	print(numbers)
	print(numbers[0])
# tuples()
# # apple:10
# # apple
# # 10
# # 10
# # 	apple, Qty = 10
# # 	banana, Qty = 15
# # 	orange, Qty = 20
# # first and only item in items: 1
# # ('second', 'third', 'fourth')
# # (2, 3, 4)
# # 1
# # (22, 33, 44, 55)
# # 22

# File I/O
def file_io():
	# following code will just create a file in this py file, it can also give another path
	# write
	# will create a fileIO.txt if not exist then write something inside
	file_path = "fileIO.txt"
	file_output = open(file_path, 'wt')
	file_output.write("1st item\n2nddd item\n3th item\n")
	file_output.close()

	# read
	file_input = open(file_path, 'rt')
	file_contents = file_input.read()
	file_input.close()
	print(file_contents)

# file_io()
# # 1st item
# # 2nddd item
# # 3th item

