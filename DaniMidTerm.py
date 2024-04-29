# Introduction 
print("Welcome to the Nutrition/Food Quiz!")
name = input("Please enter your name: ")
print(f"Hi, {name}! Let's start the quiz.")

# Define questions
questions = [
    {"question": "True or False: Is wheat bread white?", "answer": "true"},
    {"question": "Peanut butter and _____", "answer": "jelly"},
    {"question": "Which type of clothing is specifically designed to be worn during working out or sports?", "options": ["A. Sweatshirt", "B. Blazer", "C. Tracksuit", "D. Cardigan"], "answer": "C"},
    {"question": "True or False: Waffles are usually eaten for dinner", "answer": "false"},
    {"question": "What is the name of a garment worn by women that consists of a bodice and a skirt sewn together?", "options": ["A. Jumpsuit", "B. Suit", "C. Leggings", "D. Dress"], "answer": "D"},
    {"question": "True or False: Tomatoes are a fruit", "answer": "true"},
    {"question": "Shrimp and _____", "answer": "grits"},
    {"question": "Who is the Owner of Ivy Park?", "options": ["A. Beyonce", "B. Rihanna", "C. Nicki Minaj", "D. Drake"], "answer": "A"},
    {"question": "Cookies and _____", "answer": "cream"}
]

# Track correct answers
correct_answers = 0

# Quiz loop
for question_data in questions:
    print(question_data["question"])
    if "options" in question_data:
        for option in question_data["options"]:
            print(option)
        user_response = input("Enter the correct answer (A, B, C, or D): ").strip().upper()
    else:
        user_response = input("Your answer: ").strip().lower()

    if user_response == question_data["answer"]:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")

# Calculate percentage
percentage = (correct_answers / len(questions)) * 100

# Print result
print(f"{name}, your score is {correct_answers}/{len(questions)}, which is {percentage:.2f}%.")
if percentage >= 70:
    print("Congratulations, you passed!")
else:
    print("Sorry, you did not pass.")
