# Introduction
print("Welcome to the Nutrition/Food Quiz!")
name = input("Please enter your name: ")
print(f"Hi, {name}! Let's start the quiz.")

# Define questions
questions = [
    {"question": "1. True or False: Is wheat bread white?", "answer": "false"},
    {"question": "2. Peanut butter and _____", "answer": "jelly"},
    {"question": "3. How much water should people drink each day?", "options": ["A. 6-8 cups", "B. 1-2 cups","C. 3-4 cups", "D. 9-10 cups"], "answer": "A"},
    {"question": "4. True or False: Waffles are usually eaten for dinner", "answer": "false"},
    {"question": "5. What is the most important meal of the day?", "options": ["A. Snack", "B. Lunch", "C. Dinner", "D. Breakfast"], "answer": "D"},
    {"question": "6. True or False: Tomatoes are a fruit", "answer": "true"},
    {"question": "7. Shrimp and _____", "answer": "grits"},
    {"question": "8. How many eggs come in a regular size carton", "options": ["A. 6", "B. 12", "C. 8", "D. 19"], "answer": "B"},
    {"question": "9. Cookies and _____", "answer": "cream"},
    {"question": "10. How many ounces are in a cup", "options": ["A. 10", "B. 4", "C. 8", "D. 6"], "answer": "C"},
]

# Track correct answers and questions answered
correct_answers = 0

# Quiz loop
for question_data in questions:
    attempts = 0
    while attempts < 2:
        print(question_data["question"])
        if "options" in question_data:
            for option in question_data["options"]:
                print(option)
            user_response = input("Enter the correct answer (A, B, C, or D): ").strip().upper()
        else:
            user_response = input("Your answer: ").strip().upper()

        if user_response == question_data["answer"].upper():
            print("Correct!")
            if attempts == 0:
                correct_answers += 1  # Full point for correct answer on first attempt
            else:
                correct_answers += 0.5  # Half point for correct answer on second attempt
            break
        else:
            if attempts == 0:  # If it's the first attempt
                print("Incorrect! You get one more try.")
                attempts += 1
            else:
                print("Incorrect! The correct answer is:", question_data["answer"])
                break

# Calculate percentage
percentage = (correct_answers / 10) * 100

# Print result
print(f"{name}, your score is {correct_answers}/10, which is {percentage:.2f}%.")
if percentage >= 70:
    print("Congratulations, you passed!")
else:
    print("Sorry, you did not pass.")
