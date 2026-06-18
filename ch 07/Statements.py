# Break Statement
print("Break Statement")
for i in range(10):
    if i == 3:
        break # Loop terminates 
    print(i)

# Continue Statement
print("Continue Statement")
for i in range(10):
    if i == 5:
        continue # SKips the iteration
    print(i)

# Pass Statement
print("Pass Statement")
for i in range(10):
    if i == 7:
        pass # Instruct do nothing
    print(i)