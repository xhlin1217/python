# Function

def function():
	return 'function return result'
print(function())	#function return result

def function1():
	return 'function return result', 2
print(function1())	#('function return result', 2)

def add(a, b):
	return(a+b)
print(add(1,2))	# 3
print(add('hello','world')) # helloworld

def defaultParam(a, b = 2, c = 4):
	return a + b + c
print(defaultParam(1))	# 7
print(defaultParam(1, 3))	# 8
print(defaultParam(1, 3, 5))	# 9

def add(a,b):
	return a + b
def calculate(a, b, c, fun):
	return fun(a, b) * c
print(calculate(2, 4, 6, add))	# 36, (2 + 4) * 6

def outter(a):
	def inner(b):
		return a * b;
	return inner
print(outter(4)(5))	# 20

# Recursive
def factoial(a):
	if a == 1:
		return 1
	else:
		return factoial(a - 1) * a
print(factoial(5)) # 120

def sum(a):
	if a == 1:
		return 1
	else:
		return a + sum(a - 1)
def sum2(a, num = 0):
	if a == 0:
		return num
	else:
		return(sum2(a - 1, num + a))
print(sum(10)) 		# 55
print(sum2(10, 0)) 	# 55

# Lambda
f = lambda x, y : x + y
print(f(2,3))	# 5

f = lambda a: lambda b: lambda c: a * b * c
print(f(1)(2)(3))	# 6