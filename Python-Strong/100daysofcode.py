# String sclicing
"""
positive sclicing starts from 0 and negative from -1.
"""
name = "kanani het"
print(name[0:6])
print(len(name))


# Funcitons
"""
a function is a block of code that performs a specific task whenever it is called.
pass = it is a keywords that used to do nothings just pass the stuffs
example isgreater function have no body. just pass keywords and its execution status is success.
"""
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

a = int(input("enter A : "))
b = int(input("enter B : "))
calculateGmean(a,b)

def isgreater(a,b):
    pass


# Function arguments
"""
default argumnet = 
keyword argument = 
variable length argument = 
required argument = 
"""

def defaultarg(a=9 , b=3):
    print((a+b)/2)

defaultarg()