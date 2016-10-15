# we have different types of variables
# these each take up differnt amounts of memory but python takes care of that for us
var_1 = 1 # integer
var_2 = 2.345 # float
var_3 = 'three' # string

print(type(var_1))
print(type(var_2))
print(type(var_3))

# some of these we can add to gether and some we can't
print(var_1 + var_2)
print(var_1 + var_3)

# we can also re-assign the value of a variable
var_1 = 10
print(var_1)
# this can also be an equation
var_1 = var_2 + 10 - 3
print(var_1)
# we can even make var_1 equal to itself plus another number
var_1 = var_1 + 1
print(var_1)

# when we '+' two strings together we combine the words
var_4 = 'four'
print(var_3 + var_4)

# if we want to add a space between them we do this
print(var_3 + ' ' + var_4)

# we can also change what type of variables these are
# this won't always work for changing a string to an integer
print(str(var_1) + ' and ' + var_3)