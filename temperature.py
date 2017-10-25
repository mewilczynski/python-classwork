#Marta Wilczynski
#Darlene Westberg
#January 25th, 2016 ©
#temperature.py program

#Start program.
#Ask user for the temperature in Celsius right now and assign
#it to variable "celsius"
#Use the equation (celsius*1.8) + 32 and assign it to the
#variable "fahrenheit", formatting to only 3 decimal places
#Display the variable "fahrenheit"
#End program

#Prompt user for temperature in celsius, assign to variable "celsius".
celsius = float(input('What temperature is it outside, right now, in Celsius? '))
#Calculate the temperature from celsius to fahrenheit and assign this
#value to the variable "fahrenheit".
fahrenheit = (celsius*1.8)+32
#Display the new temperature in Fahrenheit.
print('In Fahrenheit, the temperature outside is', format(fahrenheit, '.3f'))
