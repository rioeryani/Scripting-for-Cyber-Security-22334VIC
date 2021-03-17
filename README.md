# Scripting-for-Cyber-Security-22334VIC
22334VIC: Scripting for Cyber Sercurity

**Class 4: For Loops**
Class Activity – Python Loops and Conditionals Practice
Student Instructions
Specific task instructions
1.	Write Python code which displays the numbers 1 to 12 separated by tabular (tab) spaces using a loop.

In your print statement make use of either sep= or end=. 
e.g. print(“hello”, end=’\t’)

Output :
1	2	3	4	5	6	7	8	9	10	11	12

2.	Write Python code which displays the numbers 12 to 1 separated by commas “,”. Make sure the last number is not displaying the comma after it.

Output :
12,11,10,9,8,7,6,5,4,3,2,1

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

4.	Write Python code which generates and displays 10 random (integer) numbers between 0 and 50, note that each time this program runs the results are different.

Hint – These 2 commands maybe useful. Modify as required:


5.	Repeat your code from the previous task and in addition to generating the 10 random numbers, display the lowest of the 10 numbers.

6.	Repeat your code from the previous task and in addition to the lowest number, display the highest and the average of the 10 numbers.
![image](https://user-images.githubusercontent.com/45652016/109716711-4b941080-7bf9-11eb-8baf-befd380711d8.png)
1.	Write a program that simulates the roll of two six sided dice.
The program should ask the user to guess the total sum of the dice.  The user has to keep guessing until they get the total correct, and the program should tell them how many tries it took.

Output :
What do you think the total of two six-sided die will be? 6
The total was 8.  Try again!

What do you think the total of two six-sided die will be? 4
The total was 11.  Try again!

What do you think the total of two six-sided die will be? 10
The total was 10.  Congratulations! It took you 3 tries to guess successfully.
![image](https://user-images.githubusercontent.com/45652016/109716774-5b135980-7bf9-11eb-9c38-2bbbcd637c73.png)

Class 7: Scripting for Cybersecurity

1. Build a function that takes the length of the three sides of a triangle and returns the area of the triangle.

area = sqrt(s(s-a)(s-b)(s-c))**0.5

s = (a+b+c)/2

2. Write a function that calculates the perimeter of a circle.
   Print the result outside the function.

3. Use Randint, write a coin toss function that takes an input of how many coin tosses and then prints    out the randomly generated coin tosses.

4. Write a script that asks the user for their name and creates a folder with that name.
   Create a testfolder to work in.
   Import the os module, use path, mkdirs, etc.

5. Use a FOR loop to ask for 5 names and create folders in your working directory.

6. Now use a while loop to ask for names for the folders. Stop when you type in "quit".
