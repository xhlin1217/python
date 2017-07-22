# File Management

# open(filename, access, buffering)
# access option: w+ read and write, wb: write it in binary format

# file reading
file = open('C:\\Users\\xing\\Desktop\\python\\python\\numbers.txt', 'r')
# file = open('numbers.txt', 'r')
print(file.read())
file.close()

# read some amoung of character of the txt file
file = open('numbers.txt', 'r')
print(file.read(4))	# read first 4 characters from the txt file
print(file.tell())	# telling the user where does the curse stop in the txt file
file.seek(7)	# tells the program which index to go for whatever reason
print(file.tell())
file.close()

# reading the file line by line
file = open('numbers.txt', 'r')
for line in file:
	print(line, end = '')
file.close()

file = open('numbers.txt', 'r')
print('File Name: ' + file.name)		# get back the file path which is using to open the file
print('isClose: ' + str(file.closed))	# checking if the file is close
print('Mode: ' + file.mode)				# checking the file reading mode
file.close()

#  file.write
# when writing the file python will auto rewrite everything in that file
file = open('writing.txt', 'w+')
file.write('hello world!! this is python')
file.seek(0)		# go back to the beginning of the file
print(file.read())
file.seek(0)		# go back to the beginning of the file
file.write("rewrite") 	#re-write the txt from the beginning with "rewrite"
file.seek(0)		# go back to the beginning of the file
print(file.read())	# rewriteorld!! this is python
file.close()