Python Assignment Part-1


Q1. Why do we call Python a general-purpose and high-level programming language?


Python is a general-purpose and high-level programming language because it is designed to be used in a range of applications and for its ease of readability.

Python is easy to understand and more natural for people to use. It is used in web development, data analysis, artificial intelligence, and scientific computing.


Q2. Why is Python called a dynamically typed language?

Python is called a dynamically typed language because there is no need to define/declare the type of variables.

For example- If I write x=5 in Python, the language automatically will understand x is an integer. I don’t need to specify if x is an integer or float or string or something else. 


Q3. List some pros and cons of Python programming language.

Pros of Python Programming Language:
1. It is easy to use, learn and maintain.
2. It has a vast collection of libraries.
3. It increases productivity.
4. It is dynamically typed.
5. It is free and open source.
6. It is an interpreted language.
7. It is a portable programming language. 

Cons of Python Programming Language:
1. It has poor memory efficiency as it consumes a lot of memory space.
2. It is weak in mobile computing.
3. It has speed limitations.
4. Underdeveloped database access.
5. It can have runtime errors.


Q4. In what all domains can we use Python?

Python can be used in the following domains-
1. Data Science
2. Web Development
3. Artificial Intelligence
4. Machine Learning
5. Automation


Q5. What are variables and how can we declare them?

Variable is the name given to a specific memory location to store values. They are like containers to store data values.

To declare a variable in Python -
•	Name the variable
•	Assign the required value to it.
•	The data type of the variable will be automatically determined from the value assigned.

For example- 
x=2
Python will take this x as an integer variable.
x=”2”
Python will take this x as a string variable.


Q6. How can we take input from the user in Python?

In Python, using the input() function, we take input from a user.

For example-
name = input("Priyanka Pal")
Print(name)



Q7. What is the default datatype of the value that has been taken as input using the input() function?

The default datatype of the value that has been taken as input using the input() function is a string datatype.



Q8. What is typecasting?

The conversion of one data type into another data type is called type casting.
It is also called type conversion.

For Example-
Converting integer to float-
int_var = 30
casted_int_var = float(int_var)

print("Int to float Typecasting = ", casted_int_var)

Output
Int to float Typecasting =  30.0
Q9. Can we take more than one input from the user using single input() function? If yes, how? If not, why?

Yes, we can take more than one input from the user using single input() function by using the split function.


Q10. What are keywords?

Keywords are some predefined and reserved words in python that have special meanings. They are used to define the syntax and structure of the Python language.

Examples of keywords- true, false, break, for, etc.


Q11. Can we use keywords as a variable? Support your answer with a reason.

We cannot use keywords as a variable as keywords have predefined meanings.
If we use keywords as variables the compiler will get confused about whether to treat them as a keyword or a variable.



Q12. What is indentation? What's the use of indentation in Python?

Indentation refers to the spaces at the beginning of a code line.

Indentation in Python is used to add white space before a statement to a particular block of code.



Q13. How can we throw some output in Python?

We can throw some output in Python using the Print function.



Q14. What are operators in Python?

Operators in Python are special symbols that carry arithmetic or logical operations. Example of operators- +, -, %, /, =, >, etc.

Q15. What is the difference between / and // operators?

/ Operator	// Operator
/ Operator or Division operator used to divide two operands.
Example- 
a = 5
b = 2

print("Divide a/b = ", a/b)

Output
Divide a/b =  2.5
	// operator or Floor division operator is used to calculate floor division.
It removes the fractional part from the normal division.
Example-
a = 5
b = 2

print("Divide a//b = ", a//b)

Output-
Divide a//b =  2




Q16. Write a code that gives the following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
text = "iNeuron"

print(text * 4)


Q17. Write a code to take a number as input from the user and check if the number is odd or even.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(num, "is an even number")
else:
   print(num, "is an odd number")


Output-
Enter a number: 888
888 is an even number


Q18. What is a Boolean operator?

Boolean Operators are those that result in the Boolean values of True and False. These include and, or and not.




Q19. What will the output of the following be?
Answer
As we know-
1 => True
0 => False

```
1 or 0 => 1

0 and 0 => 0

True and False and True => False

1 or 0 or 0 => 1
```

Q20. What are conditional statements in Python?

Conditional statements in Python are used to execute a block of code when the given condition is true or false. It is also called as decision-making statement.

In Python conditional statements are-
1. if statement
2. if-else statement
3. elif statement


Q21. What is the use of 'if', 'elif' and 'else' keywords?

Use of ‘if’ keyword- It helps to run a particular code only when a certain condition is satisfied.
For example-
x = 30
if x <= 50: 
print(“MCU is better than DC”)

Output-
MCU is better than DC

Use of ‘elif’ keyword- It is used to include multiple conditional expressions after the if condition or between the if and else conditions.
For example-
super_hero_rating = 8.4
if super_hero_rating > 9 :
   print("DC is better than MCU")
elif super_hero_rating == 9 :
   print("DC and MCU are Bhai Bhai")
else:
   print("MCU is better than DC")

Output-
MCU is better than DC

Use of ‘else’ keyword- It is used in conditional statements (if statements), and decides what to do if the condition is False.
For example-
Ironman_Love = 3000
if Ironman_Love > 2000:
  print("We Love Iron Man")
else:
  print("We can't hate Iron Man")

Output-
We Love Iron Man


Q22. Write a code to take the age of a person as input and if age >= 18 display "I can vote". If the age is < 18 display "I can't vote".

age = int(input("Enter a number: "))
if age >= 18:
   print("I can vote")
else:
   print("I can't vote")

Output-
Enter a number: 30
I can vote

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Answer-

list1 = [12, 75, 150, 180, 145, 525, 50]

even = []
odd = []

for number in list1:
 if number % 2==0:
   even.append(number)

print("even list =", even)
print("sum of evens =", sum(even))

Output-
even list = [12, 150, 180, 50]
sum of evens = 392




Q24. Write a code to take 3 numbers as input from the user and display the greatest no as output.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
else:
    largest = c

print("The largest number is", largest)

Output-

Enter the first number: 10
Enter the second number: 20
Enter the third number: 6
The largest number is 20

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
Answer
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)

Output-
75
150
145
