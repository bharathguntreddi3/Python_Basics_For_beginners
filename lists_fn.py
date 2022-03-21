b1 = [3, 33, 333, 2, 'hello', True]
b2 = [333, 33, 3, 'world', False]
b3 = [3, 33, 333, [333, 33, 3, 'hello'], 'world', False, True]
b4 = []
b5 = list(range(0,10))

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

# findind the elements 
print(b1[ :3])
print(b2[2:4])
print(b3[ :4])
print(b1[-1])
print(b3[3])
print(b3[3][2])
for i in b5:
    print(i)
    
# some operations or manipulation in lists
b1.append(3333)
print(b1)

b1[3] = 0
print(b1)

b2[0:3] = 3,33,333
print(b2)

del b1[3]
print(b1)

print(b1*2)

print(3 in b1)

a1 = [1,2,3,4,5,6,7,8,9]
a2 = a1    #Aliased
print(a1)
print(a2)

a3 = a1[:]  # cloned

print(a3)  

s1 = ['a', 'b', 'c', 'd', 'e', 'f']
s2 = ['a', 'b', 'c', 'k', 'l', 'm']
s3 = s1.intersection(s2)   #common elements
print(s3)

b1.insert(3,6)

b1.count(3)

b1.pop()   # removes last element

b1.sort()   # sorts the elements 

b1.reverse()    # reverse the list

max(b1)

min(b1)

b1.clear()   # deletes all elements form list

# Pardon Me I dont have time to type all the remaining methods of lists 
# But Dont Worry You can Go and Browse the internet for more methods in lists

