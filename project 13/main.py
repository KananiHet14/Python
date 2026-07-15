import random

n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses += 1 
    a = int(input("Guess the number : "))
    if(a > n):
        print("Lower Number Please")
    elif(a < n):
        print("Higher Number Please")
    else:
        print(f"You guess perfect number in {guesses} attempts your number is {n}")