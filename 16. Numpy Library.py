# Numpy Library

# creating numpy object
import numpy as np
a1 = np.array([2,1,3,4])
a2 = np.array([[1,2,1],[2,1,2],[1,2,3]])
a3 = np.array([[[1,1,1],[1,1,1]],[[2,2,2],[2,2,2]],[[3,3,3],[3,3,3]]])
# np.arange(start, end, step)
a4 = np.arange(10,50,10)
print('\na4: ')
print(a4)

# np.arange(stop)	# start in 0
a5 = np.arange(15)
print('\na5: ')
print(a5)

# np.arange(start, stop)
a6 = np.arange(10,20)
print('\na6: ')
print(a6)

a7 = np.arange(0.1,2,0.3)
print('\na7: ')
print(a7)

a8 = np.linspace(3,8,9)	# 9 steps from 3 to 8
print('\na8: ')
print(a8)

o1 = np.ones((2,2))	# create a matrix with size 2*2 contains all 1 
print('\no1: ')
print(o1)


o2 = np.zeros((2,2))	# create a matrix with size 2*2 contains all 0 
print('\no2: ')
print(o2)

e1 = np.empty((3,4))	# create a random number matrix with size in 3*4
print('\ne1: ')
print(e1)

e2 = np.eye(5)	# create a diagonal matirx with 1
print('\ne2: ')
print(e2)

r1 = np.random.random((5,5))	# create a 5*5 matirx with random numbers
print('\nr1: ')
print(r1)

print(a3.ndim)	# return the dimensions of a matirx
print(a2.shape)		# return the size of the matirx
print(a2.size)		# return the number of elements in the matirx
print(a2.dtype)		# return the element datatype in the matirx
print(a2.itemsize)		# return the bites of the matirx

print(a1)
print(a1.reshape(2,2))		# change the shape of the matirex


try:
	print(a3.reshape(4,6))
except Exception as e:
	print(e)

# slice matirx
print(a3)
print('--------')
print(a3[1:3])
print('--------')
print(a3[1:3, 0, 1:3])


c1 = np.arange(15)	# auto generate matirx from 1 to 14
b1 = c1 > 9			# checking boolean value for element > 9 in matirx c1
print(c1)
print(b1)

c2 = np.arange(25).reshape(5,5)	# create 5 * 5 matirx with element from 0 ~ 24
print(c2)
print(c2.max())		# return the max element of the matirx
print(c2.min())		# return the min element of the matirx
print(c2.sum())		# return the sum of every elements of the matirx
print(c2.cumsum())	# not sure
print(c2.max(axis=0))	# return the max of each row of the matirx
print(c2.max(axis=0))	# return the max of each column of the matirx
print(c2.min(axis=0))	# return the min of each row of the matirx
print(c2.min(axis=0))	# return the min of each column of the matirx


c3 = c2.copy()	# shalow copy
c3[0,0] = 100
print(c2)
print(c3)


v1 = np.array([1,1,1,1])
v2 = np.array([2,2,2,2])
print(np.vstack((v1,v2)))	# [[1 1 1 1], [2 2 2 2]]
print(np.hstack((v1,v2)))	# [1 1 1 1 2 2 2 2]



a = np.arange(1,5).reshape(2,2)
b = np.arange(2,6).reshape(2,2)
print(a)
print(b)
print(a.dot(b))			# matirx operation a * b
print(np.dot(a,b))		# matirx operation a * b
