"""
# bug = a mistake that you make while writing a program
# single = is a assignment operator its used to hand a value to a variable
# Pseudocode is a step-by-step description of an algorithm written in simple English using a code-like structure.
# print(*object) = means print take any object and print it on the screen
# print(sep=' ') = sep means saperator , sep used to saperate the objecct with space or any other character.
# print(end='\n') = \n means new line ,  end used to print the next object in new line.
# \\ = the words between the backslash used to escaping
# print(f"hello {name} !") = f string is a string that contain varibale value + string also. there f means formate.
# string.strip() = its a method that is used to remove the white-spaces from the string.
# string.capitalize() = its a method that is used to capitalize the first letter of the string.
# string.title() = its a methoda that is used to capitlized first letter of each word in the string.
# string.upper() = its a method that is used to convert the string to uppercase.
# string.lower() = its a method that is used to convert the string to lowercase.
# string.split() = its a method that is used to split the string into a list of substrings.
# int(input()) = its a function that used for type casting the input value because input value is defaltly in a string type. you can also do it by float , etc...
# Arithmatic Operators = + , - , * , / , % , // , ** used to perfeom calculation work
# relational Operators = == , != , > , < , >= , <= used to compare the values
# logical Operators = and , or , not used to combine the conditions
# Assignment Operators = = , += , -= , *= , /= , %= , //= , **= used to assign the value to a variable and change it if.
# Ternary Operators = a if condition else b used to assign the value to a variable based on a condition.
# Identity Operators = is , is not used to compare the memory location of two objects.
# bitwise Operators = & , | , ^ , ~ , << , >> used to perform bitwise operations on integers.
# round(number[,ndigits]) = its a python inbuilt function that is used to round the number to nearest integer and also you can specified it for precision by using ndigits parameter.   

"""

# name = input("enter you name : ")

# Printing the name using different methods
# print("hello " + name + " !")
# print("hello, ", end="\n")
# print(name)
# print("hello, " , name , sep="\n")


# String Methoda
# print(name.strip())
# print(name.capitalize())
# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.split("-"))


# Setup
# x = int(input("Enter number 1: "))
# y = int(input("Enter number 2: "))

# # Arithmetic Operators (+, -, *, /, %)
# print("\n--- Arithmetic Operators ---")
# print(f"{x} + {y} = {x + y}")
# print(f"{x} - {y} = {x - y}")
# print(f"{x} * {y} = {x * y}")
# print(f"{x} / {y} = {x / y}")
# print(f"{x} % {y} = {x % y}")

# # Relational Operators (<, <=, >, >=, ==, !=)
# print("\n--- Relational Operators ---")
# print(f"{x} < {y} : {x < y}")
# print(f"{x} <= {y} : {x <= y}")
# print(f"{x} > {y} : {x > y}")
# print(f"{x} >= {y} : {x >= y}")
# print(f"{x} == {y} : {x == y}")
# print(f"{x} != {y} : {x != y}")

# # Logical Operators (and, or, not)
# print("\n--- Logical Operators ---")
# print(f"({x} > 0) and ({y} > 0) : {(x > 0) and (y > 0)}")
# print(f"({x} > 0) or ({y} > 0) : {(x > 0) or (y > 0)}")
# print(f"not ({x} > 0) : {not (x > 0)}")

# # Bitwise Operators (&, |, ^, ~, <<, >>)
# print("\n--- Bitwise Operators ---")
# print(f"{x} & {y} = {x & y}")
# print(f"{x} | {y} = {x | y}")
# print(f"{x} ^ {y} = {x ^ y}")
# print(f"~{x} = {~x}")
# print(f"{x} << 1 = {x << 1}")
# print(f"{x} >> 1 = {x >> 1}")

# Assignment Operators (=, +=, -=, *=, %=)
# print("\n--- Assignment Operators ---")
# a = x  # =
# print(f"a = {a}")
# a += y # +=
# print(f"a += {y} -> {a}")
# a -= y # -=
# print(f"a -= {y} -> {a}")
# a *= y # *=
# print(f"a *= {y} -> {a}")
# a %= y # %= (Note: y cannot be 0 here)
# print(f"a %= {y} -> {a}")

# Ternary Operator (x if condition else y)
# print("\n--- Ternary Operator ---")
# ternary_result = x if x > y else y
# print(f"The larger number is: {ternary_result}")

# Identity Operators (is, is not)
# print("\n--- Identity Operators ---")
# Using lists to properly demonstrate identity in memory
# list1 = [x, y]
# list2 = [x, y]
# list3 = list1

# print(f"list1 is list3 : {list1 is list3}")
# print(f"list1 is not list2 : {list1 is not list2}")

# Round function
# number = 9.5675

# print(round(number))