"""
if = its used to check condition if its true then its execute other wise its break the flow of the program.
flowChart = its a pictorial and representable diagram of the program
elif = its used for mulitple conditions check in step by step if any one is related to true then its execute otherwise break the flow.
else = its used when all conditions are false then else execute the flow of the program.
OR = f = x+y [below is table of or operator] [only addition] [OR, |]
x   y   f
0   0   False
1   0   True
0   1   True
1   1   True

AND = f = x*y [below is table of and operator] [only multiplication] [AND, &]
x   y   f
0   0   False
1   0   False
0   1   False
1   1   True

NOT = f = x' [below is table of not operator] [opposite of the inputted value] [NOT, ~]
x       f
0       True
1       False

NOR = f = (x+y)' [below is table of nor operator] [only addition then opposite of the result] [NOT (x OR y), ~(x | y)]
x   y   f
0   0   True
1   0   False
0   1   False
1   1   False

NAND = f = (x*y)' [below is table of nand operator] [only multiplication then opposite of the result] [NOT (x AND y), ~(x & y)]
x   y   f
0   0   True
1   0   False
0   1   False
1   1   False

XOR = f = x⊕y [below is table of xor operator] [true only when inputs are strictly different] [^]
x   y   f
0   0   False
1   0   True
0   1   True
1   1   False   
"""

# if

a  = int(input("enter the numbher : "))
if (a < 5):
    print("its just example of if condition") # break
if (a > 5):
    print("its just example of if condition") # execute



# elif


if(a < 5):
    print("greater")
elif(a > 5):
    print("lesser")
elif(a == 5):
    print("equal")
else:
    print("negative number")


x = True  # Represents 1
y = False # Represents 0

# OR

if (x or y):
    print("its just example of if condition") # execute - Logical OR operator
if (x | y):
    print("its just example of if condition") # execute - Bitwise OR operator

# AND

if (x and y):
    print("its just example of if condition") # break - Logical AND operator
if (x & y):
    print("its just example of if condition") # break - Bitwise AND operator

# NOT

if (not x):
    print("its just example of if condition") # break - Logical NOT operator

# NOR

if (not (x or y)):
    print("its just example of if condition") # break - Logical NOR operator
if (~(x | y)):
    print("its just example of if condition") # break - Bitwise NOR operator

# NAND

if (not (x and y)):
    print("its just example of if condition") # execute - Logical NAND operator
if (~(x & y)):
    print("its just example of if condition") # execute - Bitwise NAND operator

# XOR

if (x ^ y):
    print("its just example of if condition") # execute - Bitwise XOR operator


# elif


if (x and y):
    print("both are true")        # Logical AND operator
elif (x or y):
    print("at least one is true") # Logical OR operator
elif (not x):
    print("x is false")           # Logical NOT operator
elif (x ^ y):
    print("inputs differ")        # Bitwise XOR operator
else:
    print("no conditions met")    # Default fallback