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


x = 5 # Binary: 0101
y = 2 # Binary: 0010

# Logical Operators

if (x > 0 and y > 0):
    print("Both x and y are positive, making the combined statement True.") # execute - Logical AND
if (x > 0 or y < 0):
    print("x is positive, so it evaluates to True regardless of y's value.") # execute - Logical OR
if (not (x == y)):
    print("x is not equal to y, so the inverted result becomes True.") # execute - Logical NOT

# Bitwise Operators

if (x & y):
    print("5 & 2 results in 0 (binary 0000), which evaluates as False.") # break - Bitwise AND
if (x | y):
    print("5 | 2 results in 7 (binary 0111), which evaluates as True.") # execute - Bitwise OR
if (x ^ y):
    print("5 ^ 2 results in 7 because the bits differ, evaluating as True.") # execute - Bitwise XOR
if (~x):
    print("~5 results in -6, and since it is not zero, it evaluates as True.") # execute - Bitwise NOT
if (x << y):
    print("Shifting 5 left by 2 positions yields 20, evaluating as True.") # execute - Bitwise Left Shift
if (x >> y):
    print("Shifting 5 right by 2 positions yields 1, evaluating as True.") # execute - Bitwise Right Shift


# elif


if (x & y):
    print("Bitwise AND yields 0, so this condition fails and is skipped.") # break - Bitwise AND
elif (x == 5 and y == 2):
    print("Both exact values match, successfully triggering this execution.") # execute - Logical AND operator
elif (x | y):
    print("Bitwise OR yields 7, but it won't run because the elif above caught it.") # break - Bitwise OR
elif (not (x > y)):
    print("x is greater than y, so NOT makes it False and it is skipped.") # break - Logical NOT
elif (x << 1):
    print("Left shift yields 10, but is skipped due to an earlier match.") # break - Bitwise Left Shift
else:
    print("No conditions were met.") # Default fallback