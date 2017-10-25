#Marta Wilczynski
#February 9th, 2016 ©
#Chapter 4 assignment program43.py

#Start program
#Prompt user for an item's cost, indicate that "0" will be the final item.
#Add each subsequent user input.
#End program when user inputs "0"
#Display the sum of all of the items.
#End program

#Initialize an accumulator variable
total = 0.0

#Prompt user for price of first item.
itemPrice = float(input("Enter the price of your item (enter 0 to end): "))

#Add the item prices the user inputs continuously until the user indicates to stop.
while itemPrice != 0:
    total += itemPrice
    itemPrice = float(input("Enter another item: "))
#Display the total amount added up
print("Your total is $", format(total, '.2f'), sep='')

