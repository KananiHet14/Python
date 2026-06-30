# by using with statement you dont need to need close th file

with open("file02.txt") as f:
    print(f.read())