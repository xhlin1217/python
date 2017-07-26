# Regular Expressions

import re
# match = re.search('hello', 'search pattern in hello world')
# print(match)			# return the match value
# print(match.re.pattern)	# return the match target
# print(match.string)		# return the match string
# print(match.start())	# return the match target start index in the match string
# print(match.end())		# return the match target end index in the match string


# regex = re.compile('pattern')
# # find the match text index
# print(regex.search('Searching pattern in text pattern..').start())
# # find all the match text
# print(regex.findall('Searching pattern in text pattern..'))
# # return if the match text mach from the beginning
# print(re.match('Match', 'Match in function test'))
# print(re.match('test', 'Match in function test'))



# pattern
def all_matches(text, pattern):
	print(pattern)
	regobj = re.compile(pattern)
	for m in regobj.finditer(text):
		print(str(m.start()) + '-' + str(m.end()) + ': ' + text[m.start() : m.end()])

all_matches('xyyxxxxxyyyyxyyxx', 'xy')
print()
all_matches('xyyxxxxxyyyyxyyxx', 'xy+')
print()
all_matches('xyyxxxxxyyyyxyyxx', 'xy*')
print()
all_matches('xyyxxxxxyyyyxyyxx', 'xy{2,}')
print()