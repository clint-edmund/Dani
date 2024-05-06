def calculate_tip(satisfaction_rating, bill_total):
    if satisfaction_rating == 1:
        tip_percent = 0.20
    elif satisfaction_rating == 2:
        tip_percent = 0.15
    elif satisfaction_rating == 3:
        tip_percent = 0.10
    else:
        print("Invalid satisfaction rating.")
        return None
    
    tip_amount = bill_total * tip_percent
    total_amount = bill_total + tip_amount
    
    return tip_amount, total_amount

def main():
    satisfaction_rating = int(input("Enter your satisfaction rating (1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied): "))
    bill_total = float(input("Enter your dining bill amount: $"))
    
    tip_amount, total_amount = calculate_tip(satisfaction_rating, bill_total)
    
    if tip_amount is not None:
        print("\nSatisfaction Level:", satisfaction_rating)
        print("Dining Bill: ${:.2f}".format(bill_total))
        print("Tip: ${:.2f}".format(tip_amount))
        print("Total: ${:.2f}".format(total_amount))

if __name__ == "__main__":
    main()