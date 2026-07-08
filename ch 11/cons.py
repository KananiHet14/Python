"""
it is a special method which is first run when we create an oblject. it is also know as a constructur.
a methods which is starts from "__" it is known as a dunder method. which is automatically called.
"""




class student:
    language = "python"
    salary = 10000
    def __init__(self , name , salary , language):
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getInfo(self):
        print(f"language is : {self.language} and salary is : {self.salary}")
    
    # static method
    @staticmethod
    def greet():
        print("hey man!")

data = student("kanani het", 15000, "python")
print(data.name , data.salary , data.language)
