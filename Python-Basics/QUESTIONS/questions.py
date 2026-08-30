# Question 1

def question1():
    name = input("Enter your name : ")
    name = name.strip().title()
    billamnt = float(input("Enter bill price : "))
    person = int(input("Enter the total person"))
    eachquantry = billamnt/person
    print(f"Hello {name} ! your bill amnt is {billamnt:.2f}Rs and each person get {eachquantry:.2f}Rs Quantry")

question1()