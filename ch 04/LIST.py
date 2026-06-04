lists = ["het" , 3.24 , 3 , False]

print(lists[3])
print(lists[0])

lists[0] = "kanani het"
print(lists)

# can do string replacement in list
# can also add new items to the list
# can do sclicing in the list
# can also do list concatenation
# can also do list repetition

# some list functions
# sort , reverse , append , insert , pop , remove , count , index , len
# example of above all the list functions
numbers = [5 , 2 , 9 , 1 , 3]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(4)
print(numbers)
numbers.insert(2 , 6)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(2)
print(numbers)
print(numbers.count(3))
print(numbers.index(6))
print(len(numbers))

# list is mutable