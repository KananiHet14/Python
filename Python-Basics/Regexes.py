"""
regular expression = a sequence of characters that forms a search pattern.
endswith = validating file extensions, filtering URLs, and verifying text formats
import re = It provides a powerful set of tools to search, extract, validate, and manipulate text based on specific patterns rather than exact string matches.
re.search() = to scan an entire string to find the first occurrence of a regular expression pattern.
. = any character except a newline
* = 0 or more repetitions
+ = 1 or more repetitions
? = 0 or 1 repetitions
{m} = m repetition
{m,n} = m-n repetitions
^ = matches the start of the string
$ = matches the end of the string or just before the newline at the end of the string
r = it means a raw string to ignore backslash escape sequence
"""

# endswith
# email = input("Enter your mail id : ").strip().lower()
# username , domain = email.split("@")
# if username and domain.endswith(".com"):
#     print("valid")
# else:
#     print("invalid")

# re library
import re

# research with expression
# email = input("Enter your mail id : ").strip().lower()
# if re.search(".+@.+" , email):
#     print("valid")
# else:
#     print("invalid")

# r string
email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")