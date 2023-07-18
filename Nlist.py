# importing RANDOM library
import random
# inputting the value of n
n = int(input("n = "))
# getting the range of wished numbers
range_start = int(input("Enter range start :"))
range_end = int(input("Enter range end :"))
# checking the maximum of n
max_n = range_end - range_start + 1
if n > max_n:
    print("You can't afford that range of elements with",n,"in total!")
    print("Maximum of n is",max_n)
# intializing
else:
    list = []
    while n > 0:
        rand = random.randint(range_start,range_end)
        if not(rand in list):
            list.append(rand)
            n -= 1
# output the list
    print(list)