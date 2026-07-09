'''
inheritance = it is the way to create a class and object from existing class and object.
-> type of inheritance: 
    1. single inheritance
    2. multiple inheritance
    3. multilevel inheritance
'''

# single inheritance
'''
class A:
    def normal(self):
        print("i am normal method of class A")

class B(A):
    def special(self):
        print("i am special method of class B")
sn1 = B()
print(sn1.normal())
'''

# multiple inheritance
'''
class A:
    def normal(self):
        print("I am normal method of class A")
class B:
    def special(self):
        print("I am special method of class B")
class C(A, B):
    def __init__(self):
        self.normal()    # Method from A
        self.special()   # Method from B
        self.greet()     # Method from C

    def greet(self):
        print("I am greet method of class C")


sn1 = C()
'''

# multilevel inheritance
'''
class employee:
    a = 1
class programmer(employee):
    b = 2
class manager(programmer):
    c=3

o = employee()
print(o.a) # print the attribute of employee class
# print(o.b) # this will give error because b is not the attribute of employee class

o = programmer()
print(o.a , o.b) # print the attribute of employee class

o = manager()
print(o.a , o.b , o.c) # print the attribute of all classes.
'''