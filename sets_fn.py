from numpy import sort


b1 = {3, 33, 333, 2, 'hello', True}
b2 = {333, 33, 3, 'world', False}
b3 = {3, 33, 333, {333, 33, 3, 'hello'}, 'world', False, True}
b4 = set()    # for empty set you cannot just simply write () 
b5 = set(range(0,10))
a1 = [3, 33, 333, 2, 'hello', True]
a2 = [333, 33, 3, 'world', False]

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

print(set(a1))    #list converted to set
print(set(a2))

print(len(b1))
print(len(b2))
print(len(b3))

print(b1 == b2)

b1.add(3333)

b1.remove(3333)

print(b1.issuperset(b2))  # checks every element in b2 is in b1

s1 = b1.union(b2)   # new ste with elements from both the sets
print(s1)

s2 = b1.intersection(b2)    # new set with elements that are common in both the sets
print(s2)

s3 = b1.difference(b2)   # new set with elements from b1 but not from b2
print(s3)

print(sorted(b1))   # new set with all elements sorted

max(b1)

min(b1)

'''
NOTE : 
        Since sets are unordered, indexing has no meaning. Set operations do not allow users
to access or change an element using indexing or slicing.

'''

