def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i



def find_better(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i




seq = [1 ,2 , 3, 5, 7, 9, 0 , 12, 16]

print "Find result = %r" % find(seq, 5)
print "Find result = %r" % find_better(seq, 5)


#-----------------------------------------------------------------#
from itertools import izip
#Construct a dictionary from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(izip(names, colors))
# {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}



#-----------------------------------------------------------------#
# Counting with dictionaries
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for c in colors:
    if c not in d:
        d[c] = 0
    d[c] += 1

print "dictionary:"
print d



#Better:
d = {}
for c in colors:
    d[c] = d.get(c,0) + 1

print "dictionary:"
print d


#Advanced:
import collections
d = collections.defaultdict(int)
for color in colors:
    d[color] += 1

print "d id "
print d


#-----------------------------------------------------------------#
class Point:
    def __init__(self, tup=(0,0)):
        self.x, self.y = tup

    def __getitem__(self, item):
        if(item == 0):
            return self.x
        else:
            return self.y

    def __add__(self, other):
        return Point((other.x + self.x, other.y + self.y))

    def __str__(self):
        return "x=%s, y=%s" % (self.x, self.y)

    def __repr__(self):
        return "<Point x:%s y:%s>" % (self.x, self.y)


p = Point((1,2))
print p
print repr(p)
print str(p)

q = Point((100, 200))

print repr(p+q)
