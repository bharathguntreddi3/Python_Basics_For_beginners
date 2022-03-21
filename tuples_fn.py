b1 = (3, 33, 333, 2, 'hello', True)
b2 = (333, 33, 3, 'world', False)
b3 = (3, 33, 333, (333, 33, 3, 'hello'), 'world', False, True)
b4 = ()
b5 = tuple(range(0,10))
b6 = 3,33,333,3333,33333,333333

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)
print(b6)

print(b1[ :3])
print(b2[2:4])
print(b3[ :4])
print(b1[-1])
print(b3[3])
print(b3[3][2])
for i in b5:
    print(i)
    
a1 = b1 + b2  # concatination
print(a1)
print(len(a1))

# We can convert a tuple into a list and can perform list operations and again convert it to tuple

s1 = list(b1)
s2 = list(b2)
s3 = list(b3)
s4 = list(b4)
s5 = list(b5)
s6 = list(b6)
s7 = list(a1)

# All the tuples mentioned above are converted to lists now we can perform the list operations as performed in lists

tuple(s1)
tuple(s2)
tuple(s3)
tuple(s4)
tuple(s5)
tuple(s6)
tuple(s7)

# All lists are converted to tuples after performing the methods




