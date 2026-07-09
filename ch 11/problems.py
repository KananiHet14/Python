"""
question 1: create a class "programmer" for storing information of few programmers working at microsoft.

question 2: write a class "calculaor" capable of finding a square , cube and squareroot of a number.

question 3: create a class with class attribute a; create an object from itand set "a" directly
            using object.a=0; does this change the class attribute?

question 4: add a static method in program 2, to greet the user with a message "hello user".

queation 5: write a class train which has a method to book a ticket , get status(no of seats available)
            and can get fare information of train running under indian railways.

question 6: can you change the self-parameter inside a class to something else (say "kanani").
            try changing self to "slf" or "kanani" and see the effects.

"""

# solution of question 1:
'''
class programmer:
    company = "microsoft"
    def __init__(self , name , salary , language):
        self.name = name
        self.salary = salary
        self.language = language

p = programmer(input("enter name : ") , input("enter salary : ") , input("enter language : "))
print(f"the name of programmer is {p.name} and salary is {p.salary} and language is {p.language} and company is {p.company}")'''


# solution of question 2:
'''
class calculator:
    def __init__(self , number):
        self.number = number
    def square(self):
        return self.number ** 2
    def cube(self):
        return self.number ** 3
    def root(self):
        return self.number ** 0.5
    
num = calculator(int(input("enter a number : ")))
print(f"the square of {num.number} is {num.square()} , cube is {num.cube()} and squareroot is {num.root()}")
'''


# solution of question 3:
'''
class demo:
    a = 10
o = demo()
o.a = 0
print(f"the value of a is {o.a}")
# this will not change the class attribute because we are changing the value of a using object and not using class name.
  and it is known as instance varioable.
'''


# solution of question 4:
'''
class calculator:
    def __init__(self , number):
        self.number = number
    def square(self):
        return self.number ** 2
    def cube(self):
        return self.number ** 3
    def root(self):
        return self.number ** 0.5
    @staticmethod
    def greet():
        print("hello user")
grt = calculator.greet()
num = calculator(int(input("enter a number : ")))
print(f"the square of {num.number} is {num.square()} , cube is {num.cube()} and squareroot is {num.root()}")
'''


# solution of question 5:
'''
from random import randint

class train:
    def __init__(self , trainNo):
        self.trainNo = trainNo
    def book(self , fro , to):
        print(f"ticket is booked in train no : {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no : {self.trainNo} is running successfully")
    def getFare(self , fro , to):
        print(f"ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = train(12399)
t.book("surat" , "mumbai")
t.getStatus()
t.getFare("surat" , "mumbai")
'''

# solution of question 6:
'''
nothing chnage there like its a specified named parameter
'''