#this program calculates the sum of a series of numbers entered by the user.

max = 5 #the maximum number

#initialize an accumulator variable.
total = 0.0

#explain what we are doing
print ('this program calculates the sum of', max, 'numbers you will enter.')

#get the numbers and accumulate them
for counter in range(max):
    number = int(input('Enter a number: '))
    total = total + number

#display the total of the numbers
print ('the total is', total)
