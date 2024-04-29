#Write a clause that takes an user input and first determines if the number is positive or negative.
#Then if the number is positive, is it greater than or less than 100 (or -100, if negative)

num = int(input("\nEnter a number between -100 and 100. "))
if num > 0:
    print("\nThe number is positive. ")
elif num == 0:
    print("\nThe number is neither negative or positive. ")
if num < 0:
    print("\nThe number is negative. ")