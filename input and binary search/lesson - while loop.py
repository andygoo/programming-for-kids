# let's use what we know about user input and make a program that
# guesses a number that we are thinking of

# the simplest way to do this would be to just go through all the number
# we can do this using a while loop

# a while loop continues while a condition is true, here is a simple example
# that guesses a number that you we had to put in
my_number = 8
guess = 0
while guess != my_number:
    print(guess)
    guess += 1

print('your number is ' + str(guess))
