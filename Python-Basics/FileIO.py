""""
open =  in Python is a built-in function used to open files on your computer, returning a file object 
'w' mode = allows you to open a file exclusively for writing if code run again its not keep old data[not append].
.write() = its a function that do help to write in file
.close() = its a functions that used to close file and save the changes
'a' mode = (Append mode) inside the open() function allows you to add new data to the end of an existing file without erasing its current content.
with.....as = statement acts as a context manager that automatically handles opening and safely closing a file.
.sorted() = this is a list function that used to sort list
reverse = True : built-in parameter used to sort data in descending order   
comma saperator = basically it is work on csv file with oindexing like row[0] , row[1] typed.
var1,var2 = Python takes the first item from that list and assigns it to var 1, and takes the second item and assigns it to var2.
key = it is thee parameter which act as a sorting rule.
lambda function = lambda function is a small, anonymous function that is defined without a name using the lambda keyword.
import csv = to read from and write to Comma-Separated Values (CSV) files and other delimited text formats.
"""

# name = input("enter your name  :  ")

# "w" mode
# file = open("FileIO.txt" , "w")
# file.write(name)
# file.close()


# "a" mode
# file = open("FileIO.txt" , "a")
# file.write(f"{name}\n")
# file.close()

# with....as
# with open("FileIo.txt" , "a") as file:
#     file.write(f"{name}\n")


# "r" mode
# with open("FileIO.txt" , "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(line.strip()) # also you can use rstrip() but its returns a copy

# sorted function in list
# names = []
# with open("FileIO.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f"hello , {name}")

# reverse
# names = []
# with open("FileIO.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names , reverse=True):
#     print(f"hello , {name}")

# CSV  file reade and open
# with open("FileIO.csv") as file:
#     for line in file:
#        row =  line.rstrip().split(",")
#        print(f"{row[0]} : {row[1]}")


# double variable declaration
# students = []
# with open("FileIO.csv") as file:
#     for line in file:
#         name , surname = line.strip().split(",")
#         students.append(f"{name} : {surname}")
# for student in sorted(students):
#     print(student)

# double variable declaration in dict and sort it
# students = []
# with open("FileIO.csv") as file:
#     for line in file:
#         name , surname = line.strip().split(",")
#         student = {"name" : name , "surname" : surname}
#         students.append(student)
# def get_name(student):
#     return student["name"]
# for student in sorted(students , key=get_name):
#     print(f"{student['name']} : {student['surname']}")


# lambda function
# students = []
# with open("FileIO.csv") as file:
#     for line in file:
#         name , surname = line.strip().split(",")
#         student = {"name" : name , "surname" : surname}
#         students.append(student)
# for student in sorted(students , key=lambda student: student["name"]):
#     print(f"{student['name']} : {student['surname']}")