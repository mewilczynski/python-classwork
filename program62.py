#Marta Wilczynski
#February 23, 2016 ©
#program62.py

#Start program.
#Open file mynumbers.txt.
#Read the lines of mynumbers.txt.
#Convert them to int values.
#Determine whether the values are even or odd.
#Take the average of the even and odd numbers, respectively.
#Display the numbers and averages.

#Define the main function.
def main():
    #Open the mynumbers.txt file and read it.
    numbersFile = open('mynumbers.txt', 'r')
    #Start totals for the sum of the even and odd numbers
    #and amount of even and odd numbers for calculations later.
    evenTotal = 0
    evenCount = 0
    oddCount = 0
    oddTotal = 0
    #Determine whether the numbers in the file are even or odd.
    for line in numbersFile:
        number = int(line)
        if number %2 == 0:
            evenTotal += number
            evenCount += 1
        else:
            oddTotal += number
            oddCount += 1
    #Close the file.
    numbersFile.close
    #Reopen the file and assign the lines of numbers to variables.
    numbersFile = open('mynumbers.txt', 'r')
    num1 = int(numbersFile.readline())
    num2 = int(numbersFile.readline())
    num3 = int(numbersFile.readline())
    num4 = int(numbersFile.readline())
    num5 = int(numbersFile.readline())
    num6 = int(numbersFile.readline())
    num7 = int(numbersFile.readline())
    num8 = int(numbersFile.readline())
    #Close the file.
    numbersFile.close()
    #Print the numbers in the file.
    print('The numbers are:', end=' ')
    print(num1, end=' ')
    print(num2, end=' ')
    print(num3, end=' ')
    print(num4, end=' ')
    print(num5, end=' ')
    print(num6, end=' ')
    print(num7, end=' ')
    print(num8)
    #Calculate the averages of the even and odd numbers, respectively.
    evenAverage = evenTotal / evenCount
    oddAverage = oddTotal / oddCount
    #Print the averages for both groups.
    print('The average for the odd numbers is', format(oddAverage, '.4f'))
    print('The avearage for the even numbers is', format(evenAverage, '.4f'))
    
#Call the main function
main()
