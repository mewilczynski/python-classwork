#Marta Wilczynski
#February 2nd, 2016 ©
#program33.py

#Start program.
#Prompt user to enter a number, assign the number to the variable "userNumber"
#Calculate the remainder of "userNumber" by (userNumber%),
#assign to variable "remainder"
#Determine whether the remainder == 0
#Depending on the remainder, determine the range of the userNumber.
#Display sentence pertaining to userNumber
#End program

#Ask the user for a number
userNumber = int(input("Give me an odd number between 30 and 80: "))
#Calculate the remainder of the number divded by 2 to determine
#if userNumber is odd
remainder = (userNumber % 2)
#Determine if the remainder is 0
if remainder == 0: #If remainder is 0, determine the range
    if userNumber > 30 and userNumber < 80: 
        print ("Your number is in range but not odd.")
    else:
        print ("Your number is not odd and not in range.")
else: #If remainder is not 0, determine the range.
    if userNumber > 30 and userNumber <80:
        print ("Your number is odd and in range.")
    else:
        print ("Your number is odd but not in range.")
