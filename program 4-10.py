# this program uses a loop to display a table of numbers and thie squares
#Get the ending limit
print ('This program displays a list of numbers (starting at 1) and their squares.')
start = int(input('Enter the starting number: '))
end = int(input('How high should I go? '))

#print the table headings
print()
print('number\tsquare')
print('--------------')

#print the numbers and their squares
for number in range(start, end + 1):
    square = number**2
    print(number, '\t', square)
