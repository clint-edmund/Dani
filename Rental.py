Days = int(input("\nHow many days was the vehicle rented for? "))
OdometerStart = int(input("\nWhat was the odometer reading at the start? "))
OdometerEnd = int(input("\nWhat was the odometer reading at the end of the rental? "))
DayRate = 40.99
MilageCharge = 0.25
ChargePerDay = Days * DayRate
Bill = (OdometerEnd - OdometerStart) * MilageCharge + ChargePerDay
print("\Your Total is", Bill)