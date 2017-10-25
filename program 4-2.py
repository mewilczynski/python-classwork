#marta wilczynski

#this program assists a technician in the process of checking a substance's temperature.

#create a variable to represent the maximum temperature
max_temp = 102.5

#get the substance's temperature
temperature = float(input("Enter the substance's Celsius temperature: "))

# as long as necessary, instruct the user to adjust the thermostat
while temperature > max_temp:
    print("The temperature is too high.")
    print("Turn the thermostat down and wait 5 minutes, then take the temperature again and enter it.")
    temperature = float(input('Enter the new Celsius temperature: '))

#remind the user to check the temperature again in 15 minutes
print ("The temperature is acceptable.")
print ("Check it again in 15 minutes.")

                        
