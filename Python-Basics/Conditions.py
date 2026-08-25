"""
if = its used to check condition if its true then its execute other wise its break the flow of the program.
flowChart = its a pictorial and representable diagram of the program
elif = its used for mulitple conditions check in step by step if any one is related to true then its execute otherwise break the flow.
"""

# if

# a = 10
# if (a < 5):
#     print("its just example of if condition") # break
# if (a > 5):
#     print("its just example of if condition") # execute



# elif
a  = int(input("enter the numbher : "))

if(a < 5):
    print("greater")
elif(a > 5):
    print("lesser")
elif(a == 5):
    print("equal")
else:
    print("negative number")