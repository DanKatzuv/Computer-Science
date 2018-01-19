# Q1
def build_list(x, y):
    return [[i * j for j in xrange(y)] for i in xrange(x)]


print
build_list(3, 4)


# Q2
def zero(lists):
    for inner in lists:
        for i in range(len(inner)):
            inner[i] = 0


l = build_list(3, 4)
print l
zero(l)
print l
# Q3
for i in xrange(1, 11):
    for j in range(1, 11):
        space = '' if i * j > 9 else ' '
        print i * j, space,
    print '\n'

# Q4
shooters = sorted(['Yarden Ghelfan', 'Roee Galili', 'Dan Bublitzki', 'Liad Zinger', 'Dan Katzuv'])
for i, name in enumerate(shooters):
    print i, name
