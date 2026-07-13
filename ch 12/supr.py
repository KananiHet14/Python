class employee:
    def __init__(self):
        print("constructor of employee class")
    a = 1

class programmer(employee):
    def __init__(self):
        print("constructor of programmer class")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__() # it can be used to call the constructor of parent class.
        print("constructor of manager class")
    c = 3

o = manager()
print(o.a , o.b , o.c)