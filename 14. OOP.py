# Object Oriented Progamming

# Abstraction (data Hiding)
# Encapsulation
# Inheritance
# Polymorphism

# class definition and object istantiation
# class a collection o attribites that are defined for nay object data members, methods

# Operator					Expression		Internally
# Addition					p1 + p2			p1.__add__(p2)
# Subtraction				p1 - p2			p1.__sub__(p2)
# Multiplication			p1 * p2			p1.__mul__(p2)
# Power						p1 ** p2		p1.__pow__(p2)
# Division					p1 / p2			p1.__truediv__(p2)
# Floor Division			p1 // p2		p1.__floordiv__(p2)
# Remainder (modulo)		p1 % p2			p1.__mod__(p2)
# Bitwise Left Shift		p1 << p2		p1.__lshift__(p2)
# Bitwise Right Shift		p1 >> p2		p1.__rshift__(p2)
# Bitwise AND				p1 & p2			p1.__and__(p2)
# Bitwise OR				p1 | p2			p1.__or__(p2)
# Bitwise XOR				p1 ^ p2			p1.__xor__(p2)
# Bitwise NOT				~p1				p1.__invert__()


class calculator:
	'this class simulates calculator operation'	# dot string, description of the class
	# first = property(getFrist, setFrist)
	# second = property(getSecond, setSecond)
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
	def getObjectData(self):
		return (self.__first, self.__second)

	def doubleFrise(self):
		return 2 * self.__first
	def doubleSecond(self):
		return 2* self.__second

	# operator overloading for adding 2 calculator object
	# following function is will use the + sign for function call, and the return typy is calaulator
	def  __add__(self, other):
		return calculator(self.getFrist() + other.getFrist(), self.getSecond() + other.getSecond())

	# for this function i try to add a elif condition for if the other type is instance of calculator object
	def __mul__(self, other):
		if (type(other) in (int, float)):
			return calculator(self.getFrist() * other, self.getSecond() * other)
		# elif isinstance(other, calaulator):
		# elif type(other) == my.object.calaulator:
		# 	return calculator(self.getFrist() * other.getFrist(), self.getSecond() * other.getSecond())
		# else:
		# 	return 'multiplier type error!!'
		else: 
			return calculator(self.getFrist() * other.getFrist(), self.getSecond() * other.getSecond())


# calss driver

try:
	c = calculator(1, 2)
	c.printdata()
	print("the first numebr: " + str(c.getFrist()))
	print("the second numebr: " + str(c.getSecond()))
	c.printdata()
	c.setFrist(10)
	c.setSecond(20)
	c.printdata()
	print(c.doubleFrise())
	print(c.doubleSecond())
except Exception as e:
	print(e)



a = calculator(2, 4)
b = calculator(1, 3)
c = (a + b)
print(str(type(c)) + ' with Value: ', end="")
c.printdata()

d = (a * 2)
print(str(a.getObjectData()) +' * 2 = ' + str(d.getObjectData()) + ', in type: ' + str(type(d)))

f = (a * b)
print(str(a.getObjectData()) + ' * ' + str(b.getObjectData()) + ' = ' + str(f.getObjectData()) + ', in type: ' + str(type(f)))



# Calss Inheritance
class vehicle:
	def __int__(self, vin, weight, manufacturer):
		self.vin = vin
		self.weight = weight
		self.manufacturer = manufacturer

	# getter
	def getVin(self):
		return self.vin
	def getWeight(self):
		return self.weight
	def getManufacturer(self):
		return self.manufacturer

	# setter
	def setVin(self, vinNumber):
		self.vin = vinNumber
	def setWeight(self, weight):
		self.Weight = weight
	def setManufacturer(self, maker):
		self.manufacturer = maker

	def printVehicle(self):
		print(self.manufacturer, self.vin, self.Weight)

	def vehicle(self):
		print('this is from vehicle object')

class car(vehicle):
	'''car Inheritance from vehicle and rewrite vehicle and __init__'''
	def __init__(self, vin, weight, manufacturer, seat):
		self.vin = vin
		self.weight = weight
		self.manufacturer = manufacturer
		self.seat = seat
	
	# getter
	def getSeat(self):
		return self.seat

	# setter
	def setSeat(self, seatNumber):
		self.seat = seatNumber

	def printCar(self):
		print(self.getManufacturer(), self.getVin(), self.getWeight(), self.getSeat())

	def vehicle(self):
		print('this is from car object, which is inheritance from vehicle object')

class Truck(vehicle):
	"""truck class instance from vehicle class and with one capacity argument"""
	def __init__(self, vin, weight, manufacturer, capacity):
		self.vin = vin
		self.weight = weight
		self.manufacturer = manufacturer
		self.capacity = capacity

	# getter
	def getCapacity(self):
		return self.capacity

	# setter
	def setCapacity(self, capacity):
		self.capacity = capacity

	def printTruck(self):
		print(self.getManufacturer(), self.getVin(), self.getWeight(), self.getCapacity())

car1 = car('Car-VIN-222', 'Car-Weight-200LB', 'Car-Manufacturer', 4)
car1.printCar()
truck1 = Truck('truck-VIN-222', 'truck-Weight-200LB', 'truck-Manufacturer', 10000)
truck1.printTruck()



class student():
	'''student'''
	numberOfStudents = 0

	def __init__(self, name):
		self.name = name
		student.numberOfStudents += 1

	def __del__(self):
		student.numberOfStudents -= 1

s1 = student('tim')
s2 = student('jack')
# all three variable point to the same address membery
print(student.numberOfStudents, s1.numberOfStudents, s2.numberOfStudents)

del s1
print(student.numberOfStudents)