# Exception Handing

# print(1/0) # ZeroDivisionError: division by zero
# file = open('file', 'r')	# FileNotFoundError: [Errno 2] No such file or directory: 'file'
# int('1.2')	#ValueError: invalid literal for int() with base 10: '1.2'

# try:
# 	a = 5 / 0
# except Exception as e:
# 	print(e)	# division by zero

# try:
# 	n = int(input('enter an integer: '))
# except ValueError:
# 	print('that is not a integer.')

# try:
# 	sum = 0
# 	file = open('numbers.txt', 'r')
# 	for number in file:
# 		sum = sum + 1.0 / int(number)
# 	print(sum)
# except ZeroDivisionError:
# 	print('Number in file equal to zero')
# except IOError:
# 	print('file not found!!')
# finally:
# 	print(sum)
# 	file.close()
# # output
# # Number in file equal to zero
# # 1.0

# a = '1'
# def raiseEsception(a):
# 	if type(a) != type('a'):
# 		raise ValueError('this is not string')
# try:
# 	raiseEsception(a)
# except ValueError as e:
# 	print(e)	
# # output 
# # the code will check if the argument is string or not 

def testCase(a, b):
	assert a < b, 'a is greater than b'
try:
	testCase(2, 1)
except AssertionError as e:
	print(e)