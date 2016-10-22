# logic statements

# a big part of programmixng is testing conditions
# is x equal to y?, is Jared older than Alison?, is it cold AND raining outside?

# to ask if things are equal we use a double = sign '=='
var_1 = 15
var_2 = 30

print(var_1 == var_2)

# we can also ask if one variable is larger or smaller than another variable
print(var_1 > var_2)

# what happens here?
print(var_2 > var_2)

# we can combine < with = to test if a variable is less than or equal to another variable
print(var_2 >= var_2)
print(var_2 <= var_2)

# we don't have to have the variable there
print(var_1 == 15)

# we can test to see if something is not equal
print(var_1 != 15)

# if statements only execute what's below them if the question is true
if var_1 == 15:
	print('var_1 is 15!')

# you can also add an else statement that will execute if the question is false
if var_1 == 12:
	print('var_1 is 12!')
else:
	print('var_1 is not 12!')

# you can also have multiple if questions
if var_1 == 12:
	print('var_1 is 12!')
elif var_1 == 13:
	print('var_1 is not 13!')
else:
	print('var_1 is not 12 or 13')