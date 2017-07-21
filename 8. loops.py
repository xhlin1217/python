# range(start, stop)
# range(start, stop, step)
# range(start, stop, step)

for i in range(1,10,2):
	print(i, end = ' ')	# 1 3 5 7 9 

for i in range(1,10):
	print(i, end = ' ')	# 1 2 3 4 5 6 7 8 9

for counter in range(10, 0, -1):
        print(counter, end = ' ')	# 10 9 8 7 6 5 4 3 2 1 

word = 'hello'
for i in range(len(word)):
	print(word[i], end = ' ')
print()
for char in word: 
	print(char, end = ' ')
print()

for i in range(0,11):
	for j in range(0,11):
		print(str(i) + '*' + str(j) + '=' + str(i*j), end = ' ')
	print()

for i in range(1,11):
	print('{:<3}|'.format(i), end = '')
	for j in range(1,11):
		print('{:>4}'.format(i*j), end = '')
	if i == 1:
		print('\n{:#^44}'.format(''), end = '')
	print('')