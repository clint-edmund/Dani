questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What is the powerhouse of the cell?", "Mitochondria"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What is the chemical symbol for water?", "H2O"),
    ("What is the largest mammal in the world?", "Blue Whale"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What is the square root of 64?", "8"),
    ("Who is credited with the theory of relativity?", "Albert Einstein"),
    ("What is the symbol for the element gold?", "Au")
]

score = 0
total_questions = len(questions)

for question, answer in questions:
    attempts = 0
    while attempts < 2:
        print(question)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answer.lower():
            print("Correct!")
            score += 1
            break
        else:
            print("Incorrect. Try again.")
            attempts += 1
    else:
        print(f"The correct answer is: {answer}")

percentage = (score / total_questions) * 100
grade = ""

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("\nYou scored {:.2f}%".format(percentage))
print("Your grade is:", grade)
