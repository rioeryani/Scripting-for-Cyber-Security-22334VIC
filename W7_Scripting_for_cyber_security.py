"""
Build a function that takes the length of the three sides of a triangle and returns the area of the triangle.
area = sqrt(s(s-a)(s-b)(s-c))**0.5
s = (a+b+c)/2
"""
a = float(input("Please input side one: "))
b = float(input("Please input side two: "))
c = float(input("Please input side three: "))

def area_triangle(a,b,c):
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

print("Area of the triangle are: " + str(area_triangle(a,b,c)))


"""
Write a function that calculates the perimeter of a circle.
Print the result outside the function.
"""
import math
r = float(input("Please input radius: "))
areaCircle = math.pi * (r ** 2)
print("Area of the circle: ", areaCircle)

"""
Use Randint, write a coin toss function that takes an input of how many coin tosses and then prints out the randomly generated coin tosses.
"""

"""
Write a script that asks the user for their name and creates a folder with that name.
Create a testfolder to work in.
Import the os module, use path, mkdirs, etc.
"""
import os
import sys

path = "/Users/rioeryani/Desktop/TestFolder/"
print(os.getcwd())
firstName = input("Tell me your first name: ")
lastName = input("Tell me your last name: ")
os.mkdir(path + firstName + lastName)

"""
Use a FOR loop to ask for 5 names and create folders in your working directory.
"""
for i in range(5):
    name = input("Please enter first name and last name: ")
    os.mkdir(path + name)
"""
Now use a while loop to ask for names for the folders. Stop when you type in "quit".
"""

path = "/Users/rioeryani/Desktop/TestFolder/"
keep_going = True
while keep_going:
    name = input("First Name and Last Name: ")
    if name.lower() != "quit":
        keep_going = True
        os.makedirs(path + name)
    else:
        keep_going = False
        sys.exit()