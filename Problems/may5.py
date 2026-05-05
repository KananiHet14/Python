# Question 1
# Personal Info Printer
# Take the user's name and age as input. Print a message like:
# Hello, Raj! You are 20 years old.
# Make sure age is stored as an integer.


name = input("Enter your name : ")
age = int(input("Enter your age : "))

print("Hello, " + name + "! You are " + str(age) + " years old.")


print("-----------------------------")


# question 2
# String Inspector

# Ask the user to enter any word. Print:
# · How many characters it has
# · It in ALL CAPS
# · Whether it starts with the letter 'a'



word = input("enter a string : ")
print(len(word))
print(word.upper())
print(word.startswith("a"))


print("-----------------------------")