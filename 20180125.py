s = 'Hello world'
s1 = 'old other old'

# Q1
print s.find('other')
print s1.find('other')
# str.find() returns the first index where the argument of the function appears. If fails, it returns -1.

# From https://docs.python.org/2/library/string.html#string.find:
# Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end].
# Return -1 on failure. Defaults for start and end and interpretation of negative values is the same as for slices.

# Q2
s1 = s1.replace('old', 'new')
print s1
#str.replace() replaces in a string the first argument with the second, so s1 becomes 'new other new'

# Q3
# a
print s[1:]
# b
print s[3:6]
# c
print s[::2]
# d
print s[:-2]