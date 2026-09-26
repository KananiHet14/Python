""""
open =  in Python is a built-in function used to open files on your computer, returning a file object 
'w' mode = allows you to open a file exclusively for writing if code run again its not keep old data[not append].
.write() = its a function that do help to write in file
.close() = its a functions that used to close file and save the changes
'a' mode = (Append mode) inside the open() function allows you to add new data to the end of an existing file without erasing its current content.
with.....as = statement acts as a context manager that automatically handles opening and safely closing a file.
.sorted() = this is a list function that used to sort list
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