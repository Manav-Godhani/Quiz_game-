# quiz game - mnv_godhani 


import random
from playsound import playsound

# ----- Quiz Questions -----
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Mumbai", "B) Delhi", "C) Kolkata", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 12", "C) 14", "D) 16"],
        "answer": "B"
    },
    {
        "question": "Who created Python language?",
        "options": ["A) James Gosling", "B) Guido van Rossum", "C) Elon Musk", "D) Bill Gates"],
        "answer": "B"
    }
]


# ----- Game Start -----
print("Welcome to the Quiz Game!\n")
score = 0

# Shuffle questions
random.shuffle(questions)

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)

    user_ans = input("Your answer (A/B/C/D): ").upper() ## Ans Input

    if user_ans == q["answer"]:
        print("Correct! ✅\n")
        score += 1
    else:
        print("Wrong! ❌ Correct answer is:", q["answer"]," ✅", "\n")

print("Your final score is:", score, "/", len(questions))

if score == len(questions):
    print("7 Crores Jackpot! 🎉🏆")
    playsound("seven_crore_amitab.mp3")
elif score >= 2:
    print("Good! Keep learning.")
else:
    print("Don't worry. Try again!")