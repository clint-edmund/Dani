# Define the list of questions and correct answers
questions = [
    "Is the sky blue? (True/False): ",
    "Is the Earth flat? (True/False): ",
    "Are dogs mammals? (True/False): ",
    "Is water wet? (True/False): ",
    "Is the sun cold? (True/False): "
]
correct_answers = [True, False, True, True, False]

# Initialize counters for correct and incorrect answers
correct_count = 0
incorrect_count = 0

# Iterate through each question
for i in range(len(questions)):
    # Prompt the user for their answer
    user_answer = input(questions[i]).strip().lower()

    # Convert the user's answer to a boolean value
    if user_answer == 'true':
        user_answer = True
    elif user_answer == 'false':
        user_answer = False
    else:
        print("Invalid input. Please enter 'True' or 'False'.")
        continue

    # Check if the user's answer matches the correct answer
    if user_answer == correct_answers[i]:
        print("Correct!")
        correct_count += 1
    else:
        print("Incorrect.")
        incorrect_count += 1

# Display the results
print("\nResults:")
print("Correct Answers:", correct_count)
print("Incorrect Answers:", incorrect_count)
