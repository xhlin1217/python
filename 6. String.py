# # basic of string
# string1 = 'this is string1'  # in python there are no different between ' and "'
# string2 = "this is string2"
# print(string1 + ", " + string2) # this is string1, this is string2
# print(string1[0]) # t, accessing the index of the string
# print(string1[-1]) # 1, accessing the last index of the string
# print(string1[-2]) # g, accessing the last second of the string

# print(len(string1)) # 15, return the size of the string

# # string cutting
# print(string1[5 : 10]) # is st, starting on the the 5th index and ends on the 10th index
# print(string1[: 10]) # this is st, starting on the the 0th index and ends on the 10th index
# print(string1[10:]) # ring1, starting on the the 10th index and ends on the last index

# # concatenation
# hello = 'hello'
# world = 'world'
# print('hello' + ' ' + 'world!')	# hello world!
# print('hello' ' ' 'world!')	# hello world!
# # print(hello world) # error
# print(hello + world) # hello world!
# print(2 * 'hello')	# print hello 2 times
# print('hello' * 2)	# print hello 2 times

# # re-assign value
# word = 'ford'
# print('L' + word[1:])	# lord


# #format method
# print('{} world, this is {}'.format('hello', 'python'))	# hello world, this is python
# print('{0} world, this is {1}'.format('hello', 'python')) # hello world, this is python
# print('{a} {b}'.format(a = 'hello', b = 'world')) # hello world
# print('{0} {b}'. format('hello', b = 'world')) # hello world
# print("{:<20}".format('hello'))	# fillin 20 space character in the right of the string
# print("{:>20}".format('hello'))	# fillin 20 characters on the left of the of the string
# # following 3 lines only apply for numbers
# print("20 in binary: {:b}".format(20))	# 10100, format the number to binary format
# print("20 in hex: {:x}".format(20))	# 14, format the number to hex format
# print("20 in octal: {:o}".format(20)) # 24, format the number to octal format

# # specific characters
# print('I\'m a string in python')	# I'm a string in python
# print("I'm a string in python")		# I'm a string in python
# print(r'c:\tim\download')	# c:\tim\download
# print('c:\\tim\download')	# c:\tim\download
# # following 2 statement are different, check by running it
# print('''\	
# 	hello
# 		world!!
# 			this is python
# 	''')
# print('''	
# 	hello
# 		world!!
# 			this is python
# 	''')