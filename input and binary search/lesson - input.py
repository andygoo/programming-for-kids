# getting input from a user is really simple in python
user_name = input('what is your name? ')

# there are three parts to this line of code. The variable that we are
# saving the input to, the text that we have appear before the user, and
# the 'input' function which makes this all work

# once we have the input from the user we can then do things with it
print('Good morning ' + user_name)

# we can even write conditional code
if user_name != 'Matt':
    print('I dont know who you are')
