items = [
    {"name": "Birthday Cake", "price": 3.75},
    {"name": "Cookies N Cream", "price": 3.25},
    {"name": "Cotton Candy", "price": 2.75},
    {"name": "Vanilla", "price": 2.00},
    {"name": "Cookie Dough", "price": 3.40}
]

print("Welcome Dani's Vending Machine!")
print("Menu:")
for i, item in enumerate(items, start=1):
    print(f"{i}: {item['name']} - ${item['price']:.2f}")

def get_item_price(items, choice):
    if choice.isdigit() and 1 <= int(choice) <= len(items):
        return items[int(choice) - 1]["price"]
    else:
        return None

total_cost = 0
receipt = []
while True:
    print("\nSelected items:")
    for selected_item, price in receipt:
        print(f"{selected_item} - ${price:.2f}")
    print("\n")

    choice = input("Enter the item number you want to purchase (or 'q' to quit): ").strip()
    if choice.lower() == 'q':
        break
    price = get_item_price(items, choice)
    if price is not None:
        selected_item = items[int(choice) - 1]["name"]
        total_cost += price
        receipt.append((selected_item, price))
    else:
        print("Invalid choice. Please select a valid item number.")

tax_rate = 0.08
total_cost_with_tax = total_cost * (1 + tax_rate)

print(f"\nTotal Cost (including 8% tax): ${total_cost_with_tax:.2f}")

while True:
    amount_due = input("Enter the amount you will pay (or 'q' to quit): ").strip()
    if amount_due.lower() == 'q':
        break
    amount_due = float(amount_due)
    if amount_due < total_cost_with_tax:
        print("Insufficient payment. Please enter an amount equal to or greater than the total cost.")
    else:
        # Calculate change
        change = amount_due - total_cost_with_tax
        dollars = int(change)
        quarters = int((change % 1) // 0.25)
        dimes = int(((change % 1) % 0.25) // 0.1)
        pennies = round(((change % 1) % 0.25 % 0.1) * 100)
        print(f"Change to be given: ${change:.2f}")
        print("Breakdown:")
        print(f"Dollars: {dollars}")
        print(f"Quarters: {quarters}")
        print(f"Dimes: {dimes}")
        print(f"Pennies: {pennies}")
        break

print("\nReceipt:")
print(f"Have a Good day and visit Dani's Vending Machine again!")
for item, price in receipt:
    print(f"{item}: ${price:.2f}")
