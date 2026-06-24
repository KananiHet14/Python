"""
def greatest(a,b,c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c     
    
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

print(f"The greatest number is : {greatest(a,b,c)}")


# f to c
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
print(f_to_c(f))


#sum of first n natural numbers
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))

# pattern function
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(5)
"""

# inch to cm
def inch_to_cm(inch):
    return inch * 2.54

inch = int(input("Enter length in inches: "))
print(inch_to_cm(inch))