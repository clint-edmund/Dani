# Daniela Baptiste

"""
This is a program that computes and displays the amount of money charged for a customer's vehicle rental

1. Ask the user the number of days the vehicle was rented
2. Ask the user the vehicle's odometer reading at the start of the rental period
3. Ask the user the vehicle's odometer reading at the end of the rental period
4. All vehicles have a $40.99 daily rate
5. Mileage charge 0.25 for each mile driven
6. Compute the daily rate with each mile driven
7. Output the result

"""

Days = int(input( "How many days was the vehicle rented for?"))
OdometerStart = int(input("What was the odometer reading at the start of the rental period?"))
OdometerEnd = int(input("What was the odometer reading at the end of the rental period?"))
DayRate = 40.99
MileageCharge = 0.25
Bill = (OdometerEnd - OdometerStart) * MileageCharge + DayRate
ChargePerDay = Days * DayRate
print("Your total is", Bill,)
