#Marta Wilczynski
#February 2nd, 2016 ©
#order32.py

#Start program.
#Get the number of t-shirts being purchased from the user,
#assign to variable "amountOfShirts".
#Calculate amountOfShirts * 12.99, assign to variable "priceOfShirts".
#Assign number 8.99 to variable "shipping".
#Determine discounts by looking at amount of shirts being bought.
#If amountOfShirts >= 12, calculate (priceOfShirts) - (priceOfShirts * 0.3)
#If amountOfShirts >= 6 and <=11,
#calculate (priceOfShirts) - (priceOfShirts * 0.2) + shipping
#If amountOfShirts >= 3 and <=5,
#calculate (priceOfShirts) - (priceOfShirts * 0.1) + shipping
#If amountOfShirts == 1 or == 2, calculate (priceOfShirts) + shipping
#Assign calculated price of shirts to variable "finalPrice".
#Display the amount needed to pay.

#Ask user for amount of t-shirts
amountOfShirts = int(input("How many shirts are you buying? "))
#Assign base price of shirts to variable "priceOfShirts"
priceOfShirts = float(amountOfShirts * 12.99)
#Assign shipping price to variable "shipping"
shipping = float(8.99)
#Determine whether or not the user qualifies for discounts
if amountOfShirts >= 12:
    finalPrice = ((priceOfShirts) - (priceOfShirts * 0.3))
else:
    if amountOfShirts >= 6 and amountOfShirts <= 11:
        finalPrice = ((priceOfShirts) - (priceOfShirts * 0.2) + shipping)
    else:
        if amountOfShirts >= 3 and amountOfShirts <= 5:
            finalPrice = ((priceOfShirts) - (priceOfShirts * 0.1) + shipping)
        else:
            finalPrice = ((priceOfShirts) + shipping)
#Display the final price of the shirts.
print ("Your total comes to $", format(finalPrice, ',.2f'), sep='')
    
