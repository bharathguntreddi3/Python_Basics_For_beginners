import turtle
from tkinter import *

# # normal 
print("Hello World")

# # string
myStr = ('H','e','l','l','o','  ','W','o','r','l','d','!')
for s in myStr:
    print(s,end='')
    
# # user
while True:
    print("How many times you did like to print hello world : ", end="")
    try:
        b = int(input())
        for i in range(b):
            print("Hello World!")
        break
    except ValueError:
        print("\nInvalid Input!..Try Again!\n")
       
# Turtle and Tkinter



root = Tk()

lbl_display = Label(root, text='Hello, World!')
lbl_display.pack()

turtle.write('Hello, World!')
turtle.done()

root.mainloop()




