#Marta Wilczynski
#Darlene Westberg
#January 25th, 2016 ©
#cashier.py program

#Start program.
#Ask user for the price of the item, assign to variable "priceOfItem".
#Ask user for the amount of that item being bought, assign value
#to variable "amountOfItem".
#Assign value 0.07 to variable "calculateTax"
#Multiply price*amount, assign to variable "subtotal"
#Multiply subtotal*calculateTax, assign to variable "salesTax"
#Add subtotal+salesTax, assign to variable "total"
#Display the variable "subtotal"
#Display the variable "salesTax"
#Display the variable "Total"
#End program

#prompt user for the price of the item
priceOfItem = float(input('How much does the item cost? Please input only digits. '))
#prompt user for amount of item
amountOfItem = int(input('How many are you buying? '))
#Assign 0.07 to "calculateTax"
calculateTax = 0.07
#Calculate subtotal
subtotal = priceOfItem*amountOfItem
#Calculate sales tax
salesTax = subtotal*calculateTax
#Calculate total
total = subtotal+salesTax
#Display subtotal
print('Subtotal: $', format(subtotal, ',.2f'), sep='')
#Display sales tax
print('Sales Tax: $', format(salesTax, ',.2f'), sep='')
#Display total
print('Total: $', format(total, ',.2f'), sep='')
