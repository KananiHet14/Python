# String = string is a sequence of characters.

# String can be defined in three ways:
# 1. Using single quotes: 'Hello, World!'
# 2. Using double quotes: "Hello, World!"
# 3. Using triple quotes: '''Hello, World!''' or """Hello, World


# a string in python can be sliced for getting a part of the string.
# strings are immutable in python, which means that we cannot change the value of a string after it is created.
# the indexing of string starts from 0 to (length-1) in python.

# syntax = sl = name[ind_start:ind_end]

name = "kanani het"
print(len(name)) # length of the string
name_sliced = name[0:6]
print(name_sliced) # slicing the string from index 0 to 5


# negrative indexing : negative indexing can also used as shown in figure above. -1 corresponds to the (length - 1) index , -2 to (length - 2).
#  if there any black of index then it will be considered as length.
# example
print(name[1:]) # is same as print(name[1:5])
print(name[1:6])


# slicing withskip value : we can provide a skip values as a part of slicing like by using step value.

word = "amazing"
print(word[1:6:2]) #2 is like it print the character one leave and then print leaved after character and so on. it is called step value.