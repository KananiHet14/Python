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
# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# a = int(input("enter A : "))
# b = int(input("enter B : "))
# calculateGmean(a,b)

# def isgreater(a,b):
#     pass


# Function arguments
"""
Default Argument = we can provide a default value while creating a function.
Keyword Argument = we can provide arguments with the key = value , in this we can changew the order of arguments are passed doesn't metter. 
                   interpreter recognize the arguments by the parameter name.
Required Argument = we must be rpovide value of the parameter that  we have passed as the function argument. you can't change the order.
Variable Lenght Argument : 1. [Arbitrary Argument] = while creating function , pass a * before  the parameter name while defining a function.
                                                      it accessed by processing them in the form of tuple.
                           2. [Keyword Arbitrary Argument] = while creating function , pass a ** before  the parameter name while defining a function.
                                                      it accessed by processing them in the form of dictionary.
return = The return statement is used to return the value of the expression back to the calling the function.
"""
# Default Argument
def defaultargument(a=10 , b=7):
    print(f"average is : {(a+b)/2}")
defaultargument()

# Keyword Argument
def keywordargument(b=20 , a=7):
    print(f"average is : {(a+b)/2}")
keywordargument()

# Required Argument
def requuiredargument(a , b , c=10):
    print(f"average is : {(a+b+c)/3}")
requuiredargument(20,10)

# Variable Length Argument [Arbitrary Arguments]
def arbitraryargument(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(f"Average is : {sum/len(numbers)}")
arbitraryargument(5,6)

# Varialble Length Argument [Keyword Arbitrary Argument]
def KeywordArbitraryArgument(**name):
    print("hello" , name["fname"] , name["mname"] , name["lname"])
    print(type(name))
KeywordArbitraryArgument(mname = "het" , lname = "nileshbhai" , fname = "kanani")

# Return
def arbitraryargument(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
c = arbitraryargument(5,6)
print(c)