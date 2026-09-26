""""
open =  in Python is a built-in function used to open files on your computer, returning a file object 
'w' mode = allows you to open a file exclusively for writing
.write() = its a function that do help to write in file
.close() = its a functions that used to close file and save the changes
"""

name = input("enter your name  :  ")

file = open("names.txt" , "w")
file.write(name)
file.close()