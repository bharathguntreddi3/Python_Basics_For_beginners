import numpy as np 
a = np.array([1,2,3])
print(a)


import numpy as np
a = np.array([1,2,3], dtype = 'int16')
b = np.array([[1,2,3],[4,5,6]])
print(a)
print(b)
# a.ndim , b.ndim get dimensions

# a.shape , b.shape  get vector dimensions

# a.dtype , b.dtype  get memory size and datatype

#a,itemsize , b.itemsize  gets byte size

#a.nbytes   gets no of byte size


# np.zeros(5)  get zero matrix
#np.zero(2,3)  get 2d matrix

#np.full((2,2),99)  #2 by 2 matrix with all  numbers 99

#np.full(a, 4)    a array values replacing with 4

#np.random.rand(4,2)  #generates a random values of matrix

#np.random.int_sample(a.shape   #gives random matrix with shape a

#np.random.randint(7, size(3,3)   random matrix with integers

#np.random.randint(-3,6, size(4,4)

#np.identity(5)    produce a identity matrix

#r3 = np.repeat(a, axis = 0)  #repeats array

output = np.ones(5,5)
print(output)

z = np.zeroes(3,3)
z[1,1]= 9
print(z)
output[1:4,1:4] = z
print(output)


copy()  #just copies the elements

a = np.array([1,2,3,4,5,6])


np.matmul(a,v)  #matrix multiplication


np.linalg.det(a)  #determinent

np.sum()

a.reshape(2,4)  #reshapes the matrix

np.vstack([a,b])   #combines to arrays to one matrix vertically

np.hstack([a,b])   #combines to arrays to one matrix horizontally

data = np.genfromtxt('data.txt', delimiter = ',')   #import a data or text file and load 
data = data.astype('int32')
print(data)

data > 50   #gets true or false values greater than 50 in the data

data[data > 50]   #gets the values in a order way
np.any(data >50, axies = 0)  #in a specific rows 

((data > 50) & (data < 100))   #between the values

(~(data > 50) & (data < 100))    #not



















