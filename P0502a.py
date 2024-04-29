# Daniela Baptiste
"""This is a program that prompts the user for an integer N in the range 0 to 9
Algorithm:
1. Ask the user to enter a number 0 through 9
2. Initialize height
3. if/else ("error")
4. Write a for loop
5. Print a number triangle whose Height = num """
"""Part A"""
height = False
while not height:
    user_response = input("Enter a value from 0 to 9: ")
    if user_response.isdigit():
        N = int(user_response)
        if 0 <= N <= 9:
            height = True
        else:
            print("Error input. Invalid input. Please enter a value from 0 to 9: ")
    else:
        print("Error input. Please enter an integer. ")

# Printing triangle to screen
for a in range(1, N + 1):
    for b in range(1, a + 1):
        print(b, end="")
    print()


"""Part B"""
height = False
while not height:
    user_response = input("Enter a value from 0 to 9: ")
    if user_response.isdigit():
        N = int(user_response)
        if 0 <= N <= 9:
            height = True
        else:
            print("Error input. Invalid input. Please enter a value from 0 to 9: ")
    else:
        print("Error input. Please enter an integer. ")

# Printing triangle to screen
for a in range(1, N + 1):
    print(" " * (N - a), end=" ")
    for b in range(1, a + 1):
        print(b, end=" ")
    print()



