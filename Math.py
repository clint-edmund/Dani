# Daniela Baptiste

"""This is a program to solve Everyday Math problems
They are each solved by a function
Included:
Distance Kilometers to Miles (KM = .62M
Temperature (Celsius to Fahrenheit F = 9/5 * C * 32
Gratuity = 18% of original Return tip and total bill
Discount Sale price based on an item's initial price and & discount
Weight (pounds to kilograms) K = P/2.2
"""
import math

# Define print_menu() function before main() function
def print_menu():
    print("Select from the following options")
    print("1. Distance Kilometers to Miles")
    print("2. Temperature C to F")
    print("3. To compute to Gravity")
    print("4. Discount Sale")
    print("5. Pounds to Kilograms")
    print("6. Leave the program")

# this code calculates tips
def Calculate_Tips():
    TotalBill = float(input("how much was the bill? "))
    Tip_Amount = TotalBill * 0.18
    Tip_Amount = round(Tip_Amount, 2)
    return Tip_Amount, TotalBill

# this code calculates temperature
def Temperature():
    Celsius = float(input("enter a celsius Temperature "))
    Fahr = 9/5 * Celsius + 32
    return Fahr

# this code calculates distance
def Distance():
    Kilos = float(input("what is the distance in Kilometers "))
    Miles = Kilos * .62
    return Miles

# this code calculates discount price
def Discount_Price():
    Initial_price = float(input("Input an initial price "))
    DiscAmt = float(input("What percent discount? "))
    Discount = Initial_price * DiscAmt/100
    Sale_Price = Initial_price - Discount
    return Sale_Price

# this code calculates pounds to kilograms
def Pounds_to_Kilograms():
    Weight_In_Pounds = float(input("enter a weight in pounds "))
    Weight_In_Kilograms = Weight_In_Pounds / 2.2
    return Weight_In_Kilograms

def main():
    choice = 0
    while choice != 6:
        print_menu()
        choice = int(input("What would you like to do? "))
        if choice == 1:
            Dis = Distance()
            print("The converted distance is", Dis)
        elif choice == 2:
            Tem = Temperature()
            print("The Celsius temperature is", Tem, "Fahrenheit")
        elif choice == 3:
            Tip, Tot = Calculate_Tips()
            print(f"The bill was {Tot} and the tip was {Tip}")
        elif choice == 4:
            SaleAmount = Discount_Price()
            print("The sale price is ", SaleAmount)
        elif choice == 5:
            Kilos = Pounds_to_Kilograms()
            print("The amount in kilograms is", Kilos)
        elif choice == 6:
            print("Thank you for using my program!!!!")

# Call the main function to start the program
main()
