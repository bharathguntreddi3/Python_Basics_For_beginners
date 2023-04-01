import cmath
import random
import datetime
# from calender import *

n = random.randint(1,100)
print(n)       #print random numbers

rand_list = []
for i in range(1,11):
    n = random.randint(1,50)
    rand_list.append(n)
print(rand_list)        #print random numbers list

#celcious to faherenheit

# cel = int(input("enter temperature"))
# fah = ((cel*9)/5) + 32
# print(fah)

#swap two numbers
# a = int(input(""))
# b = int(input(""))
# temp = a
# a = b
# b = temp
# print(a)

#import calender
# print month dates
yy = int(input(""))
mm = int(input(""))
print(calender.month(yy, mm))

#to print leap year

def check_year(n):
    if n%400==0 or n%100!=0 and n%4==0:
        print("leap year")
    else:
        print("not leap year")

check_year(2012)


#prime number or not

def prime(n):
    while(n>0):
        for i in range(2,n+1):
            if a%i==0:
                print("not prime")
            else:
                print("prime")

prime(5)


#prime numbers in given range

low = int(input(""))
high = int(input(""))

for i in ragne(low, high+2):
    while(i>1):
        for j in range(2,i):
            if i%j==0:
                break
            else:
                print(i)



#factorial

n = int(input(""))

fact = 1
while(n>=0):
    for i in range(1,n+1):
        fact = fact * i
    print(fact)




# # #factorial
# # num = int(input("Enter a number: "))    
# # factorial = 1  
# # if num<0:
# #     print("error")
# # else:
# #     for i in range(1,num + 1):    
# #         factorial = factorial*i   
# #     print("The factorial of",num,"is",factorial) 


# #multiplication table
# # n = int(input("enter a number:"))
# # for i in range(1,13):
# #     print(n,"*",i,"=",n*i)



# #fibanocci series
# # n = int(input(""))
# # n1 = 0
# # n2 = 1
# # i = 0
# # while i<n:
# #     print(n1)
# #     next = n1 + n2
# #     n1 = n2
# #     n1 = next
# #     i = i+1

# # armstrong number

# # n = int(input(""))
# # sum=0
# # temp = n
# # while temp>0:
# #     d = temp%10
# #     sum = sum + d*d*d
# #     temp = temp//10
# # if sum  == n:
# #     print(n)
# # else:
# #     print("not")

# #armstrong numbers in the given range

# low = int(input("1"))
# high = int(input("2"))
# for i in range(low, high + 1):
#     sum = 0
#     temp = i
#     while(temp>0):
#         d = temp%10
#         sum = sum + d*d*d
#         temp = temp//10
#     if i == sum:
#         print(i)


#sum fo natural numbers
# n = int(input(""))
# sum = 0
# while(n>0):
#     sum = sum + n
#     n = n - 1
# print(sum)



def fact(n):
    fact = 0
    fact = fact*fact(n-1)
    print(fact)
    
fact(3)
    