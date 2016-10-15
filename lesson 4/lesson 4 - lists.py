# Lists

# lists are a very useful way in python of storing a bunch of things together.

# we can create a list several different ways
my_list = [1, 2, 3, 4] # this is a list with values
my_empty_list = [] # this is an empty list

# we can ask python how many items are in the lists using the len funciton
print(len(my_list))

# We can also iterate over the lists
for x in my_list:
    print(x)

# we can ask the list to give us a specific entry
print(my_list[2])
# lists, and many things in programming, start counting at 0

# We can also change what values are at specific points in the list
my_list[2] = 10
print(my_list)
