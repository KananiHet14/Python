class employee():
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of employee class is {cls.a}")

e = employee()
e.a = 10 #instance attribute
e.show()
