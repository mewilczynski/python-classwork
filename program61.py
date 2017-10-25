#Marta Wilczynski
#February 23, 2016 ©
#program61.py

#Start program.
#Import Random.
#Generate 8 random integers between 10-100 inclusive.
#Write these numbers to a text file called mynumbers.txt, each integer on its
#own line.
#end program.

#define the main function.
def main():
    #open file.
    numbersFile = open('mynumbers.txt', 'w')
    #import random.
    import random
    #generate 8 random integers and write them to the file.
    for count in range(8):
        number = random.randint(10, 100)
        numbersFile.write(str(number) + '\n')
    #close the file.
    numbersFile.close()
    print('The numbers have been written to the file.')
#call the main function.
main()
    
