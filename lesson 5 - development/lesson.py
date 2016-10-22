# so we've learned about variables, if statements, and loops
# now let's put them all together

# example 1:
# In this example we have a bunch of fruit. Now we want to divide
# up the fruit using a loop so that Jared gets all the oranges and Issac
# gets all the apples
# In the end we print out how many of each they have
fruit = ['apple', 'orange', 'apple' ,'apple', 'orange']

jared = []
issac = []

for f in fruit:
    if f == 'apple':
        issac.append(f)
    else:
        jared.append(f)

print('Issac has ' + str(len(issac)) + ' apples')
print('Jared has ' + str(len(jared)) + ' oranges')
