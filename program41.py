#Marta Wilczynski
#February 2nd, 2016 ©
#Chapter 4 assignment program41.py

#Start program
#Import math since we will be using PI
#Set up a range of numbers, using the for loop.
#Calculate area of a circle with "radius", where the equation
# will be area = (PI * (radius ** 2))
#Calculate circumfrence with "radius",
# where the equation will be circumfrence = (2 * PI * radius)
#Format and display the radii, areas, and circumfrences.
#End program

#import math
import math
#Start the loop, 
for radius in range(10, 51, 10):
    area = (math.pi * (radius ** 2)) #Calculate the area
    circumfrence = (2 * math.pi * radius) #calculate the circumfrence
    print(format(radius, '5,.3f'), '\t', format(area, '9,.3f'), '\t', format(circumfrence, '7,.3f')) #Format the numbers into a column, aligning the decimal points and going to 3 decimal points
    
