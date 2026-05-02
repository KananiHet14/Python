# typecasting is the process of converting one data type to another data type
# there are two types of typecasting
# 1. implicit typecasting
# 2. explicit typecasting
# implicit typecasting is done by the python interpreter automatically
# explicit typecasting is done by the programmer using the built-in functions

a = 10
b = float(a) # explicit typecasting
print(type(a) , type(b))

a = int(input("enter a number :"))
print(type(a))
b = int(input("enter a number :"))
print(type(b))
print(a+b)