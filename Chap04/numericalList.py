# Looping Through an Entire List
# author: Teo Espero
#         BS Software Development
#         BS Cloud and Systems Administration
#         Western Governors University

# two ways of making a list of numbers

# 1
# define an empty list
myFirstList = []

# create a loop that will append the numbers
# to the list
for value in range(1,20):
    myFirstList.append(value)

# define a new list and use the list function
# to populate it
myNumbers = list(range(1,20))

# print our lists
print(myFirstList)
print(myNumbers)