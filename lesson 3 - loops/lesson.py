# loops

# programming is great because it can do a lot of things
# faster than what we can do.

#  one way we do this is with loops

# if we want to print out the numbers from 0 to 10 we can do it this way
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# or we can do it this way
for i in range(11):
	print(i)

# in a for loop we specify a variable (in this case i) and that
# variable gets larger by each time we go through the loop

# the range() function starts at zero and goes up to, but not including, the
# number in the ()

# the loop will automaticly start at 0, unless we tell it otherwise
for i in range(5, 11):
	print(i)
