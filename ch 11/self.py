class student:
    language = "python"
    salary = 10000
    def getInfo(self):
        print(f"language is : {self.language} and salary is : {self.salary}")
    # static method
    @staticmethod
    def greet():
        print("hey man!")

data = student()
data.getInfo()
data.greet() # this is for static method.