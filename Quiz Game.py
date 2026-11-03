questions = [
    {
        "question": "Which country hosts the Monaco Grand Prix?",
        "options": ["A. Italy", "B. Monaco", "C. France", "D. Spain"],
        "answer": "B"
    },
    {
        "question": "What does DRS stand for in Formula 1?",
        "options": [
            "A. Drag Reduction System",
            "B. Driving Racing System",
            "C. Dynamic Racing Speed",
            "D. Direct Rotation System"
        ],
        "answer": "A"
    },
    {
        "question": "How many points does a driver receive for winning a Grand Prix?",
        "options": ["A. 15", "B. 18", "C. 25", "D. 20"],
        "answer": "C"
    },
    {
        "question": "Which flag signals the end of an F1 race?",
        "options": [
            "A. Red Flag",
            "B. Yellow Flag",
            "C. Blue Flag",
            "D. Chequered Flag"
        ],
        "answer": "D"
    },
    {
        "question": "What is the name of Ferrari's F1 racing team?",
        "options": [
            "A. Mercedes-AMG",
            "B. Scuderia Ferrari",
            "C. Red Bull Racing",
            "D. McLaren Racing"
        ],
        "answer": "B"
    }
]

def start_quiz():
    score = 0

    print("\n===== PYTHON QUIZ APPLICATION =====")

    for i, q in enumerate(questions, start=1):
        print("\nQuestion", i)
        print(q["question"])

        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct answer:", q["answer"])

    print("\n===== QUIZ RESULT =====")
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(questions) - score)
    print("Final Score:", score, "/", len(questions))

    if score == 5:
        print("Excellent Performance!")
    elif score >= 3:
        print("Good Performance!")
    else:
        print("Keep Practicing!")


while True:
    start_quiz()

    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("Thank you for playing!")
        break
