# function ia a group of statements performing a specific task.
'''
def avg() :
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    average = (a + b + c) / 3
    print(average)


avg()
'''

# types of functions : 1] built in 2] user defined

# parameters and arguments
def goodDay(name):
    print("Good Day " + name)

goodDay("Kanani")

# return statement
def add(a,b):
    return a+b

result = add(5, 10)
print(result)

# default parameters
def goodDay(name, ending="Thank you!"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Kanani")
# if you provide a diff vale then its considered a diff value
