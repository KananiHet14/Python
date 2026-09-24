"""
"UnitTest.py" is only for function that i made. for testing or writing code there is "unit_testing.py" file.
"""


"""
firstly testing square function in the anotherfile which name is "unit_testing.py"
assert = keyword in Python is a debugging aid used to test if a specific condition in your code evaluates to True.
         If the condition is True, the program continues executing normally. If the condition evaluates to False,
         Python immediately halts the program and raises an AssertionError.
pytest it is a python inbuilt unit testing library.
pytest.raisesErrorType) = is used to assert that a specific block of code raises an expected exception
"""
import pytest
def main():
    x = int(input("Enter the number : "))
    print(f"number square is : {square(x)}")

def square(n):
    return n*n

if __name__ == "__main__":
    main()