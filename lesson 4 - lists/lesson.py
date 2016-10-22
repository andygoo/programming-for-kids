# Lists

# lists are a very useful way in python of storing a bunch of things together.

# we can create a list several different ways
my_list = [1, 2, 3, 4] # this is a list with values
my_empty_list = [] # this is an empty list

# can print everything in a list by using the print statement
print(my_list)

# we can ask python how many items are in the lists using the len funciton
print(len(my_list))

# We can also iterate over the lists
for x in my_list:
    print(x)

# sometimes we may start with an empty list and then want to fill it.
# to add something to a list we just use the append funciton
my_empty_list.append(1)
print(my_empty_list)

# we can ask the list to give us a specific entry
print(my_list[2])
# lists, and many things in programming, start counting at 0

# We can also change what values are at specific points in the list
my_list[2] = 10
print(my_list)

# we can also test to see if something is in a list
print(4 in my_list)

# we can then use this in a if statement

if 4 in my_list:
    print('4 is in the list')
