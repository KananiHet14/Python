# readlines function
# f = open("file02.txt")

# lines = f.readlines()

# print(f"lines here : {lines} , and type of lines is : {type(lines)}")

# f.close()

# readlines by using loop but step by step lines come
filename = open("file02.txt" , "r")
for i in filename:
    print(i)