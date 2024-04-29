# Daniela Baptiste

"""Write a program that asks for the user's first middle and last names
It should print a greeting using theFirst and Middle initial and the last name
There should be periods after the initials.
Algorithm
Ask the user for their three names
Use [0] to get the first initial of the first name and middle name
Print the greeting (individualized greeting)
"""

FirstName = input("enter your first name")
MiddleName = input("enter your middle name")
FirstInitial = FirstName[0]
MiddleInitial = MiddleName[0]

#Then get the last name
LastName = input("enter your last name")
# print the message
print("Howdy", FirstInitial,".", MiddleInitial, ".", LastName)
