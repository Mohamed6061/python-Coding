# Course Content
# 1 Output functon:Print function,Variables
# 2 Inputs:Input functon,Typeconversion
# 3 Operators:Arithmetic coperators,Logical operators
# 4 Decision making:If statement,Else statement
# 5 Flow control: Forloop
# 6 Flow control: Whileloop
# 7 Collect on data: Lists,Tuples,Sets,Dictonaries
# 8 Functions:Define functions, Call function

# ----------- Print Function -------------#
# output functions
print("Hello, World!")
print(12)
print(12.3)

# Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 1
y = "one"
# print(x + y) #Error
# F-String Formating
print(f"this var one {x} , this var two {y}")
print(f"{x} {y}")

# ---------------- Creating Variables --------------#

x = 5
y = "John"
print(x)
print(y)

# Varibles names

# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# ----------------- Data type ------------------------#
# datatype
# float
# str
# int 
# bool
# list
# set
# dict

var_int = 1
print(var_int)
print(type(var_int))

var_float = 12.3
print(var_float)
print(type(var_float))

var_bool = True
print(var_bool)
print(type(var_bool))

var_list = [12 , 34 , 34 , "one" ]
print(var_list)
print(type(var_list))

# ------------ data conversion ---------#
# convert intager
x = 12.6
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# covert float
x = float(1)     # x will be 1.0
print(x)
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(float("3.4"))

print(int(35.88))

# bool ==> int
x = False 
print(int(x))

x = -12
print(bool(x))

# ------------- Input function ---------------#
input_value = input()
print(type(input_value))
print(input_value)

# Calc Age
input_value = input("enter your age : ")
print(f"You was born in {2024 - int(input_value)}")


# ------------- String methods-------#
txt = "Hello, World"
print(txt[:5])

print(txt.lower())  # Covert text to lower case
print(txt.upper())  # convert text to upper case

txt = "   text   "
print(txt.strip())   #remove spaces
print(txt.replace('t' , "Q")) # replace 't' with 'Q'

txt = "Hello python"
x = txt.split()  # convert string to list
print(x)
print(" ".join(x)) # convert list ot string 

varlist = ["one" , "two" , "three"]
print(varlist[0])  # print the first element
print(varlist[-1]) # print the last element

t = "my name is moemen"
# how to convert ot list
v = t.split()
print(v[0])

# Exercise
sentence = input("Enter a sentence: ")
sentence = sentence.split()
print(sentence)
print("this first index " , sentence[0])
print("this last index ", sentence[-1])


txt = "this are apple"
print(txt.index("are"))  # get index number

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")
if word in sentence:
    print(f"Word found at index {sentence.index(word)}")
else:
    print("Word not found.")

txt = "my name Moemen"
print(txt[1:4])

# Exerxise
string = input("Enter a string: ")
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))
print("Extracted substring:", string[start:end])

# ----------------- If ------------------#
# Case 1
if 3 > 2 :
    print("done")
elif 2 == 2 :
    print("equal")
else :
    print("failed")
    
# Case 2
if 3 > 2 :
    print("done")
if 2 == 2 :
    print("equal")
else :
    print("failed")
    