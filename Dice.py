# first analisys
import random
rand_num = random.randint(1 , 6)
# input
num =int( input ("Enter your number : "))
# intializing and output
i = 0
while i == 0 :
    if rand_num != num :
        print("You losed")
        print("Quitting the program")
        i = 1
    if rand_num == num :
        print("That's true!")
        print("You won another roll")
        rand_num = random.randint(1 , 6)
        num =int( input ("Enter your number : "))
