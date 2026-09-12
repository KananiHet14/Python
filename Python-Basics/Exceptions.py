"""
exception = its an error that occurs during the execution of a program and disrupts the noraml flow of its instructions.
ZeroDivisionError: Raised when you try to divide a number by zero (1 / 0).
ValueError: Raised when a function gets an argument of the right type but an inappropriate value.
TypeError: Raised when an operation is applied to an object of an inappropriate data type.
FileNotFoundError: Raised when you attempt to open a file that does not exist.
IndexError: Raised when you try to access an index that is out of range for a list.
NameEroor: Python simply does not recognize the "name" you are trying to use
try: Runs the risky code that might cause an error. its a keywords
except: Catches and handles the error if one occurs. its a keywords
else: Executes only if no exception occurs in try. its a keywords
finally: Runs regardless of what happens useful for cleanup tasks like closing files. its a keywords
get_int = checks if it is a valid integer, and automatically loops to re-ask the user if they type something invalid. cs50 library
get_float = same as int (just catch is its for decimal values) cs50 library
get_string = (its for strings) cs50 library
"""

import cs50

# Basic example of try:except
# n = 10
# try:
#     res = n/0
# except ZeroDivisionError:
#     print("can't devided by zero")


# finally keyword
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Caught division by zero error.")
# finally:
#     print("This block always executes.")

# # proper code
# try:
#     # 1. ZeroDivisionError
#     # result_div = 5 / 0

#     # 2. ValueError
#     # user_age = int("twenty")

#     # 3. TypeError
#     # total_cost = "Price: " + 19.99

#     # 4. IndexError
#     # colors = ["red", "blue"]
#     # selected_color = colors[5]

#     # 5. NameError
#     print(missing_variable)

# except ZeroDivisionError:
#     print("ZeroDivisionError caught.")

# except ValueError:
#     print("ValueError caught.")

# except TypeError:
#     print("TypeError caught.")

# except IndexError:
#     print("IndexError caught.")

# except NameError:
#     print("NameError caught.")

# else:
#     print("Success: No errors occurred.")

# finally:
#     print("Finally: This code always runs.")
