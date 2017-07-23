# Object Oriented Progamming

# Abstraction (data Hiding)
# Encapsulation
# Inheritance
# Polymorphism

# class definition and object istantiation
# class a collection o attribites that are defined for nay object data members, methods


class calculator:
	'this class simulates calculator operation'	# dot string, description of the class
	def __init__(self, first, second):
		if(type(first) not in (int, float)) or type(second) not in (int, float):
			raise Exception('Args are not numbers!')
		self.__first = first
		self.__second = second

	# getter
	def getFrist(self):
		return self.__first
	def getSecond(self):
		return self.__second

	# setter
	def setFrist(self, val):
		if(type(val) not in (int, float)):
			raise Exception('set value type error in setFrist')
		self.__first = val
	def setSecond(self, val):
		if(type(val) not in (int, float)):
			raise Exception('set value type error in setSecond')
		self.__second = val

	def printdata(self):
		print(self.__first, self.__second)

	def doubleFrise(self):
		return 2 * self.__first
	def doubleSecond(self):
		return 2* self.__second


# try:
# 	c = calculator(1, 2)
# 	c.printdata()
# 	print("the first numebr: " + str(c.getFrist()))
# 	print("the second numebr: " + str(c.getSecond()))
# 	c.printdata()
# 	c.setFrist(10)
# 	c.setSecond(20)
# 	c.printdata()
# 	print(c.doubleFrise())
# 	print(c.doubleSecond())
# except Exception as e:
# 	print(e)

