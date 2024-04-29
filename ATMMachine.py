# Daniela Baptiste
""" Using a menu develop a simple ATM that allows deposit, withdrawal, check
balance and exit. Initial balance is $1000. The program uses while loop.

Algorithm:
1. Initalize the initial balance to $1000
2. Display the menu
3. Take user choice
4. Do the math and show new balance with message
    a) for deposits, add to current balance
    b) for withdrawls, subtract from current balance
    c) for check balance simply display with a message

5. When the user selects, quit display a goodbye message
"""
Balance = 1000.00

choice = 1

while choice >= 1 and choice < 4:
    print("Enter a number from 1-4")
    print("1, Deposit Money")
    print("2, Withdraw Money")
    print("3, Check Balance")
    print("4, Exit")
    choice = int(input("What is your choice"))
    if choice == 1:
       deposit = float(input("how much is the deposit?"))
       Balance = Balance + deposit
       print("Your new balance is $",Balance, "you deposited", deposit)
    elif choice == 2:
        withdraw = float(input("how much do you wish to withdraw?"))
        Balance = Balance - withdraw
        print("You withdrew", withdraw, "your new balance is $", Balance)

    elif choice == 3:
        print("your current balance $", Balance)
    elif choice == 4:
        print("Thank you for stopping by! See you soon :)")
    else: print("Invalid entry")
        
             
