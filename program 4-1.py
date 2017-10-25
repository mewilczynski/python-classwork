#Marta Wilczysnki
#February 2nd, 2016

#this program calculates sales commissions

#create a variable to control the loop.
keepGoing = 'y'
#calculate a series of commissions
while keepGoing == 'y':
    #get a salesperson's sales and commision rate.
    sales = float(input('Enter the amount of sales: '))
    commRate = float(input('Enter the commission rate: '))

    #calculate the commission
    commission = sales * commRate

    #display the commision
    print ('The commission is $', format(commission, ',.2f'), sep='')

    #see if the user wants to do another one
    keepGoing = input('Do you want to calculate another commission? Enter y for yes: ')
    
