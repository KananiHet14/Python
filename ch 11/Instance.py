"""
there is a same3 thing in class and instance then when we print it we saw always instance item
"""

class student:
    language = "python"
    salary = 10000

data = student()

data.language = "java"
print(data.language," ",data.salary)