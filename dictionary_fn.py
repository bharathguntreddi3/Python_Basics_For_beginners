d1 = {
    "Reg No" : 123,
    "Name" : "james",
    "Age" : 21,
    "Branch" : "CSE"
}

d2 = {
    "Reg No" : 124,
    "Name" : "carl",
    "Age" : 21,
    "Branch" : "EEE"
}

d3 = {
    "Reg No" : 125,
    "Name" : "ross",
    "Age" : 21,
    "Branch" : "CSE"
}

d4 = {
    "Reg No" : 126,
    "Name" : "mary",
    "Age" : 21,
    "Branch" : "ECE"
}

d5 = {
    "Reg No" : 127,
    "Name" : "james",
    "Age" : 21,
    "Branch" : "MECH"
}

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)

print(len(d1))
print(len(d2))
print(len(d3))
print(len(d4))
print(len(d5))

# We cannot access elements by slicing 
# Insted we can access them by its keys

d1["gender"] = "Male"  # we can add a new key-value pair
print(d1)

del d1["gender"]    # delete a key-value pair
print(d1)

print(d1.items())

print(d1.keys())

print(d1.values())

print(d2.update(d1))    # adds all elements from dictionary d1 to d2

# looping through dictionaries

for i in d1:
    print(i)    # displays keys
for i in d1:
    print(d1[i])    # keys to dictionary and displays the elements
    
# converting list to dictionary
c1 = ["name", "age", "gender", "branch"]
c2 = ["james", 21, "MALE", "CSE"]
z = zip(c1,c2)    # Creating ZIP class Object 
d = dict(z)
print(d)

st = "name = James, age = 21, gender = Male, branch = CSE"
s1=st.split(',')
s2=[]
for i in s1:
    x = i.split('=')
    s2.append(x)
print(dict(s2))

d1.clear()   #clears all the key-value pairs
print(d1)