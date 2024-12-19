# Revision

# int
# float
# str
# list
# tuble
# bool

x = "13"
y = int(x)

f = float(x)
     #  012345
txt  = "hello python"
print(txt.upper())
print(txt[:5])

print(txt.split()[0])

x = 4
if x > 0 :
    print("positive")
else :
    print("negative")
# ----------------------------------------
# Revision on Task

# Task 1
# Print multiple items with separator
name = "Ali" 
age = 30
city = "Cairo"

print(f"my name is {name}, age {age}, I lives in {city}")
# ----------------------------------------
# Task 2
str_num = "123"
# # Convert string to integer
print(int(str_num))
# # Convert string to float
print(float(str_num))

float_num = 9.8
# # Convert float to integer
print(int(float_num))
# # Convert float to string
print(str(float_num))

int_num = 10    
# # Convert integer to string
print(str(int_num))
# # Convert integer to float
print(float(int_num))

# # Task 3
num1 = 15
num2 = 5
result = num1 / num2
print(type(result)) 

# # Task 4
# # Calculate Area for rectangular
# # user will input length and width

# l = float(input("Enter length : " ))
# w = float(input("Enter width : "))
# Area = l * w

# print(f"Area = {l} * {w} = {Area}")
# ----------------------------------------

# Operators:Arithmetic coperators,Logical operators

a = 10
b = 3
c = a + b
print("Addition (a + b):", c ) 

print("Subtraction (a - b):", a - b) 

print("Multiplication (a * b):", a * b) 

print("Division (a / b):", a / b)

print("Modulus (a % b):", a % b)

a = 9
if a%2 ==0 :
    print("ok")

print("Floor Division (a // b):", a // b)

print("Exponentiation (a ** b):", a ** b) 

# === Logical Operators ===
a = 3
b = 20
c = 10
# AND -  OR  - NOT

# print((b > 15))
print("Logical AND (x > 5 and y > 15):", (a > 5) and (b > 15) ) 

#    a    and     b 
#   true  and true  =  true
#   false and true  =  false 
#   true  and false = false 
#   false and false = false


print((a < 5) or (b > 15))
print((a > 5) or (b < 15))

#    a    or     b 
#   true  or true  =  true
#   false or true  =  true 
#   true  or false = true 
#   false or false = false

print("Logical NOT (not (x > 5)):", not (a > 5))
a = 3
b = 20
c = 10

# print( a > 5 and b > 10 and c > 15 )
print( a < 5 and b > 10 and c < 15 )
print( a > 5 or b > 10 or c < 15 )
print( a < 5 and b > 10 and not c < 15 )

# ----------------------------------------

x = 10

if x > 10 :
    print(True)
elif x == 10 :
    print("is equal")     
else:
    print(False)


if x >= 10 :
    print("x is more than 10 ")
elif (x == 10 ) :
    print("is equal ten")
else :
    print(False)

# ----------------------------------------

x = 30
y = 50
if  x > 20 and y < 60:
    print("Both conditions are true.") 
if x > 40 or y < 60:
    print("At least one condition is true.")  


# Exercise one
score = int( input("enter score"))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Exercise Two : Finding the largest of three numbers
num1 = 10
num2 = 20
num3 = 15
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)  # Output: The largest number is: 20
else:
    print("The largest number is:", num3)


# Exercise Three

x ,y ,z = input("enter num1 num2 operator : ").split()
print(x)
print(y)
print(z)


num1, num2, operator =  input("enter num1 num2 operator : ").split()
num1, num2 = float(num1) , float(num2)
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2) 
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")
    
# Exercise Four  Checking if a number is even or odd
number = int(input())
if number % 2 == 0:
    print("The number is even.")   
else:
    print("The number is odd.") 
