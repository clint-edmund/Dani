import random

random_numbers = set()  # Create an empty set

# Keep adding random numbers to the set until it has 6 unique elements
while len(random_numbers) < 6:
    random_numbers.add(random.randint(1, 36))

# Convert the set to a list and print the selected numbers
random_numbers = list(random_numbers)
print("Randomly selected numbers:", random_numbers)
