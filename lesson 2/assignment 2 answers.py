# Minecraft Example

# create a variable called health with a value of 100
health = 100

# make another variable called arrow with a value of 10
arrow = 10

# make another variable called armor that is either true or fales, you choose
armor = True

# now let's pretend that you got hit by an arrow, now you need to subtract the arrow
# value from your health. But if you have armor you will only take half the damage
# make an if statement that will subtract the right amount of health and then 
# print your new health value
if armor == True:
	health = health - (arrow / 2)
else:
	health = health - arrow

print('New health is ' + str(health))
