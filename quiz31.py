#Marta Wilczynski
#January 26th, 2016 ©
#Chapter 3 assignment quiz31.py

#Start program
#Display "Let's take a quiz!"
#Begin question 1
#Assign correct answer for question 1 to the variable "correctAnswer1".
#Prompt user to answer the question "What do you call a horse with one horn?",
#assign answer to the variable "userAnswer1".
#Determine if "userAnswer" == "correctAnswer1"
#if yes, print "Correct! Good job."
#if not, display "Incorrect. The correct answer is Unicorn"
#Display "Ready for another question?"
#Begin question 2
#Prompt user for one number, assign to variable "numberOne"
#Prompt user for another number, assign to variable "numberTwo"
#Calculate the product of numberOne*numberTwo,
#assign to variable "correctAnswer2"
#Prompt user for the product of the two numbers provided, assign this value to
#the variable "userAnswer2"
#Determine if userAnswer2 == correctAnswer2
#if yes, display "Correct! Your math skills are great."
#if not, display "Incorrect. The correct answer is "correctAnswer2""
#End program

print("Let's take a quiz!")
print()
#Start first question
#Assign correct answer to variable "correctAnswer1"
correctAnswer1 = 'Unicorn'
#Assign user's input to question to variable "userAnswer1"
userAnswer1 = input('What do you call a horse with one horn? ')
#Determine if correctAnswer1 == userAnswer1
if userAnswer1 == correctAnswer1:
    print('Correct! Good job.')
else:
    print('Incorrect. The correct answer is', correctAnswer1)
print()
print('Ready for another question?')
print()    
#Start second question
#Assign user's input to variable "numberOne"
numberOne = int(input('Give me a single digit: '))
#Assign user's second input to variable "numberTwo"
numberTwo = int(input('Now give me another single digit: '))
#Calculate the product of the two user given numbers
correctAnswer2 = numberOne*numberTwo
#Ask the user for the product of the two user given numbers
userAnswer2 = int(input('Please give me the product of these numbers: '))
#Determine if the userAnswer2 == correctAnswer2
if userAnswer2 == correctAnswer2:
    print('Correct! Your math skills are great.')
else:
    print('Incorrect. The correct answer is', correctAnswer2)
