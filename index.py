
'''---------------OOP---------------------'''

# object or instance is the realworld application
# class is the design or the blueprint for making an object
# method is nothing but function in OOP



class robo:      # created a class robo 
    def current(self):            # method
        print("features")


# created 3 objects for the class robo
r1 = robo()    # created object or instance com1 for class robo
r2 = robo()
r3 = robo()

# print(type(r1))

# robo.current(r1)   # calling the class with the class and object name

# r1.current()  # calling the class with object name

# r1.current()  # calling the class with the object name

'''-----------------------------------------------------'''

class computer:

    def __init__(self, cpu, ram):   #initializing variables __int__ prints automatically no need of calling it
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)

com1 = computer('i5', 16)
com2 = computer('ryzen 3', 8)

# com1.config()
# com2.config()

'''-----------------------------------------------------'''

class computer:

    def __init__(self):
        self.name = "burma"
        self.age = 29

    # def update(self):
    #     self.name = "ravi"

    def compare(self, other):      #created  a method compare  to compare the values
        if self.age == other.age:
            return True
        else:
            return False

 


c1 = computer()
c1.age = 30
c2 = computer()

# if c1.compare(c2):
#     print("same")
# else:
#     print("different")

# c1.name = "paloma"


# # c1.update()

# print(c1.name)
# print(c1.age)



'''-------------------------------------------------------'''

# variables
# variables defined in the __init__ are instance variables
# variables defined outside the __init__ are class variales


class car:

    #variables defined outsode of the __init__ class variables

    wheels = 4

    def __init__(self):
        #instance variables mil and com
        self.mil = 10
        self.com = "bmw"



c1 = car()
c2 = car()

c1.mil = 8

# print(c1.com, c1.mil, c1.wheels)
# print(c2.com, c2.mil, c2.wheels)

# car.wheels = 5

# print(c1.wheels)
# print(c2.wheels)

'''------------------------------------------'''
#types of methods instance method, class method, static method

class student:

    college = "vignan"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2 
        self.m3 = m3

    def avg(self):     #instance method passing self that belongs to a class
        return (self.m1 + self.m2 + self.m3)/3 

    def get_m1(self):
        return self.m1      #accessor fetching the values get method

    def set_m1(self, value):
        self.m1 = value     #mutator changing the values by set method
        return self.m1

    @classmethod   #decorator  to use info as a class method
    def clg_info(cls):      #when working with class variables we use cls // while working with instance variables we use self
        return cls.college

    @staticmethod
    def info():    #static method no self or cls required to initialize static method is neithor instance method nor class method 
        print("blahhhhhh")     #static method nothing details with the class variables or instance variables

s1 = student(90,89,99)
s2 = student(79,98,100)

# print(s1.avg())
# print(s2.avg())

# print(student.clg_info())  #calling the class method 
# print(s1.get_m1())
# print(s2.set_m1(66))

# student.info()

'''--------------------------------------------'''



class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()      #the object of the laptop class is created in the outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:     #inner class 

        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student("chanu", 24)
s2 = student("tejes", 6 )

# s1.show()


'''---------------------------------------------------------'''

# INHERENTENCE 
# 

class A:    #parent class

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):       #child/sub class inhertting all features of A

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(B):      #grand child class inherits the features of the both A abd B class 

    def feature5(self):
        print("feature 5 working")

    def feature6(self):
        print("feature 6 working")


# a1 = A()

# a1.feature1()
# a1.feature2()

# b1 = B() 

# b1.feature3()
# b1.feature4()

# c1 = C()

# c1.feature5()
# c1.feature6()

# c1.feature1()

#----------------------------------------------------

class A:    #parent class

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:       #B is not inheriting the features of the class A

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):      #grand child class inherits the features of the both A abd B class 

    def feature5(self):
        print("feature 5 working")

    def feature6(self):
        print("feature 6 working")


# a1 = A()

# a1.feature1()
# a1.feature2()

# b1 = B() 

# b1.feature3()
# b1.feature4() 

# c1 = C()

# c1.feature5()
# c1.feature6()

# c1.feature1()


#------------constructor in  inherentnce -----------

class A:    #parent class

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:       #child/sub class inhertting all features of A

    def __init__(self):
        super().__init__()    #super is a method or keyword you can access all the features of the parent  class   
        print("in B init")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):

    def __init__(self):
        super().__init__()     #super accesss all elements of super class
        print("in C init")

    def feat(self):
        super().feature2()


# super() first calls the intit of the parent class then later calls the child class init

# super()   access the values of the parent class but doesnt inherit super class

# a1 = B()    # prints in B init first tries to find init of then then init of A

# a2 = C()    # constructor of A calls a method __init__

# method resolution order(MRO) - goes from left to right, first prints A and then prints B

# a2.feat()    # super() can also be used to call the other methods also not only init method

# to represent super class we use super()


'''-------------------polymorphism-----------------------------------'''

# polymorphism - one thing can take many forms
#duck typing - if there is an object which has a method that execute

class pycharm:

    def execute(self):
        print("compile")
        print("run")

class editor:

    def execute(self):
        print("convert return")
        print("check spell")

class laptop:

    def code(self, ide):
        ide.execute()

ide = pycharm()

# lap1 = laptop()
# lap1.code(ide)



#operator overloading - 

a = 3
b = 3
# print(a+b)
# print(int.__add__(a,b))  # int.__add_() method also adds the numbers
# # print(str.__add__(a,b))  # str for string the strings are concatinated
# print(int.__sub__(a,b))   #subtracts a, b
# print(int.__mul__(a, b))   #multiplies a, b

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1 
        m2 = self.m2 + other.m2
        print(m1)
        print(m2)
        s3 = student(m1, m2)
        return s3

    def __gt__(self, other):
        s1 = self.m1 + self.m2 
        s2 = other.m1 + other.m2 
        if s1 >s2:
            return True
        else:
            return False

    def __str__(self):
        #return self.m1, self.m2     #to print the valus of the s1 object
        return '{} {}'.format(self.m1, self.m2)    #prints the format in strings 



s1 = student(50, 90)
s2 = student(10, 78)

s3 = s1 + s2 
# print(s3.m1)

# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")

# print(s1)    #prints the values in strings
# print(s2)



'''-----------method overloading-------------'''
# method overloading is the methods with same name but diferent arguments

class student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s



s1 = student(5, 10)

# print(s1.sum(5,3))


'''------------------method overriding-------------------'''
# method overriding the child method overriding the parent method

class A:

    def show(self):
        print("in A show")

class B(A):
    
    def show(self):
        print("in B show")    #here show in B class override the method in A class



a1 = B()
a1.show()


#public member: members of class are accessable from outside of the class
class student:
    schlname="abc schl"

    def __init__(self,name, age):
        self.name = name
        self.age = age


std = student("burma",30)
# print(std.age)
std.age = 20
# print(std.age)


#protected members: members of class are accessable from within the class and available in the sub class
class student:
    _sclname = "abc school"     #  protected members is denoted by the _variabel

    def __init__(self,name,age):
        self._name = name
        self._age = age


std = student("burma",30)
# print(std._name)


class student:

    def __init__(self,name):
        self.name = name

    @property     # @property decorator is used to make method name() as property
    def name(self):
        return self._name

    @name.setter   #n@name.setter decorator is used to method overloads of the name() method as property setter method
    def name(self,newname):
        self._name = newname     #_name is protected


# private (__prefix makes a varaiable private)

class student:
    __schname = "abc school"

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

        def __display(self):
            print("this is private method")


std = student("burma","30")
print(std._student__name)   #to show the variables use   _object._class__variable


# ABSTRACTION
#ABC - Abstract Base Class
#Abstract Method - containing a declaration but no definition

from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("run")

class whiteboard(computer):
    def write(self):
        print("write")

class programmer:
    def work(self,com):
        print("solve bugs")
        com.process()

com2 = laptop()
# com3 = whiteboard()
prog1 = programmer()
prog1.work(com2)

# com1 = computer()
# com1.process()



