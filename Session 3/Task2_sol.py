# Exercise 1: Evaluate and Compare
# Write a program to:

# Take two numbers as input from the user.
# Perform the following arithmetic operations: addition, subtraction, multiplication, division, and modulus.
# Check if the first number is greater than the second and print the result using a logical operator.
# Check if at least one of the numbers is even.

# Example Input:
# Enter first number: 12
# Enter second number: 5

# Expected Output:
# Addition: 17  
# Subtraction: 7  
# Multiplication: 60  
# Division: 2.4  
# Modulus: 2  
# Is the first number greater than the second? True  
# Is at least one number even? True  

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

# Check logical conditions
is_greater = num1 > num2
is_even = (num1 % 2 == 0) or (num2 % 2 == 0)

# Display the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
print(f"Is the first number greater than the second? {is_greater}")
print(f"Is at least one number even? {is_even}")

# ----------------------------------------------------------
# Exercise 2: Logical Operations Challenge
# Given three inputs 
# 𝑥,z,𝑦 
# Check and print if all three numbers are greater than 10.
# Check and print if at least one number is less than 5.
# Print the logical negation of  𝑥 > 20

# Example Input:
# Enter x, y, z: 15 12 8

# Expected Output:
# All numbers are greater than 10: False  
# At least one number is less than 5: False  
# Logical NOT (not x > 20): True  

# Take input from the user
x, y, z = input("Enter x, y, z: ").split()
x, y, z = int(x), int(y), int(z)
 
# Check if all numbers are greater than 10
all_greater_than_10 = (x > 10) and (y > 10) and (z > 10)

# Check if at least one number is less than 5
at_least_one_less_than_5 = (x < 5) or (y < 5) or (z < 5)

# Logical NOT of (x > 20)
logical_not_x_greater_20 = not (x > 20)

# Print results
print(f"All numbers are greater than 10: {all_greater_than_10}")
print(f"At least one number is less than 5: {at_least_one_less_than_5}")
print(f"Logical NOT (not x > 20): {logical_not_x_greater_20}")

# ----------------------------------------------------------
# Exercise 3: Grade Checker
# Write a program to take a percentage score from the user and determine the grade:

# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60

# Example Input:
# Enter your score: 85

# Expected Output:
# Grade: B
# Take the percentage score as input from the user
score = float(input("Enter your score: "))

# Determine the grade
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the grade
print(f"Grade: {grade}")

# ----------------------------------------------------------
# Exercise 4: Simple Calculator
# Take two numbers and an operator as input and perform the respective operation. Include an option to calculate the floor division (//). If the operator is invalid, print an error message.

# Example Input:
# Enter operator and two numbers  : // 10 3 

# Expected Output: 
# Result: 3

# Take operator and two numbers as input
operator , num1, num2 = input("Enter operator (+, -, *, /, //, %) | num1 | num2 : ").split()
num1, num2 = float(num1) , float(num2)
 
# Perform the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
elif operator == '//':
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Error: Division by zero"
elif operator == '%':
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

# Print the result
print(f"Result: {result}")

# ----------------------------------------------------------

import random
target = random.randint(1, 20)

print(target)
