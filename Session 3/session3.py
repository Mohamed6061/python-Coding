# --------------------------------------------
# Course Content
# 1 Output functon:Print function,Variables  ==> Done
# 2 Inputs:Input functon,Typeconversion      ==> Done 
# 3 Operators:Arithmetic coperators,Logical operators ==> Done
# 4 Decision making:If statement,Else statement   ==> Done
# 5 Flow control: Forloop
# 6 Flow control: Whileloop
# 7 Collect on data: Lists,Tuples,Sets,Dictonaries
# 8 Functions:Define functions, Call function

# Syntax:
# for variable in sequence:
#     # Code to execute

for i in range(6):
    print(i)
    
for x in range(2, 6):
  print(x)
  
for x in range(2, 30, 3):
  print(x)
  
for x in range(6):
  if x == 3: break
  print(x)

name = "Mohamed abdel fatah"
list =  ["apple", "banana", "cherry"]
for x in name :
    # x = ""
    print(x)

for l in list :
    print(l)


list1 = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in list1 : 
    # x  = "red"
    # x  = "big"
    # x  = "tasty"
    
    for y in fruits :
        print(x, y)
    #     x  = "red"
    #     y = "apple"
         
    #      x = "red"
    #     y = banana
         
    #      x = "red"
    #     y = cherry
        
        
    #     x  = "big"
    #     y = "apple"
         
    #      x = "big"
    #     y = banana
         
    #      x = "big"
    #     y = cherry
        
    #     x  = "tasty"
    #     y = "apple"
         
    #      x = "tasty"
    #     y = banana
         
    #      x = "tasty"
    #     y = cherry
        
        
        
    #     1 ==> ("red" , "apple")
    #     2 ==> ("red" , "banana")
    #     3 ==> ("red" , "cheery")

# multiblication Table for 10
n = 10
for i in range(1, 13):
    print(f"{i} x {n} = {i * n}")
 
# multiblication Tables for all numbers
for i in range(1, 13):
    print("multiblication table " , i)
    for y in range(1,13):
        print(f"{i} x {y} = {i * y}")

# -----------------------------
i = 0
while i < 20 :
    print("ok")
    i += 1 
    print(i)
    if i == 10 :
        break

passwod = 123
user_input = ""

while user_input != "exit" :
    user_input = input("Enter ")
    print("you entered " , user_input)
    print("not existed, still inside loop")
