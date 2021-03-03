"""
1.	Write Python code which displays the numbers 1 to 12 separated by tabular (tab) spaces using a loop.

In your print statement make use of either sep= or end=.
e.g. print(“hello”, end=’\t’)

Output :
1	2	3	4	5	6	7	8	9	10	11	12


print("Give me three numbers")
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
num3 = input("Enter number 3: ")

if (num1 > num2) and (num1 > num3):
    largestNum = num1
elif (num2 > num1) and (num2 > num3):
    largestNum = num2
else:
    largestNum = num3
print("Largest Number is: " + largestNum)

print("---------------------------------------------------")


2.	Write Python code which displays the numbers 12 to 1 separated by commas “,”. Make sure the last number is not displaying the comma after it.

Output :
12,11,10,9,8,7,6,5,4,3,2,1



print(*reversed(range(1,13)), sep=", ")

print("--------------------------------------------------")


3.	Write Python code which starts with the number 1 and then displays the result of halving the previous number until the result is less than 0.001.

Output :
1.0
0.5
0.25
0.125
0.0625
0.03125
0.015625
0.0078125
0.00390625
0.001953125


num = int(input("enter your number: "))

while True:
    num /= 2
    if num > 0.001:
        print(num)

print("--------------------------------------------------")

4.	Write Python code which generates and displays 10 random (integer) numbers between 0 and 50, note that each time this program runs the results are different.
5.	Repeat your code from the previous task and in addition to generating the 10 random numbers, display the lowest of the 10 numbers.
6.	Repeat your code from the previous task and in addition to the lowest number, display the highest and the average of the 10 numbers.



import random

list = random.sample(range(1,50),12)
print(list)

smallest = min(list)

print("the minimum number is: ", smallest)

largest = max(list)

print("The largest number is: ", largest)

average = sum(list) / len(list)

print("the average is: ", average)

print("--------------------------------------------------")

7.	Write a program that simulates the roll of two six sided dice.
The program should ask the user to guess the total sum of the dice.  The user has to keep guessing until they get the total correct, and the program should tell them how many tries it took.

Output :
What do you think the total of two six-sided die will be? 6
The total was 8.  Try again!

What do you think the total of two six-sided die will be? 4
The total was 11.  Try again!

What do you think the total of two six-sided die will be? 10
The total was 10.  Congratulations! It took you 3 tries to guess successfully.

"""
import random
from random import randint

print("Welcome to the guessing game! I am going to roll a dice and you are going to guess the total sum of the dice.")
print("rolling two dice....")

#roll the first dice from random
dice1 = randint(1,6)
print(dice1)
#roll the second dice from random
dice2 = randint(1,6)
print(dice2)

diceSum = int(dice1) + int(dice2)
print(diceSum)
count = 0
while True:
    try:
        guess = int(input("What do you think the total of the two sided die will be?"))
        count += 1
    except ValueError:
        print("Please enter a valid input!")
        continue
    if guess != diceSum:
        print(f"The total was {diceSum}. Try again!")
        continue
    else:
        print("Congratulations, it took " + str(count) + " tries to guess successfully.")
        break





