# Interview Panic AI

role = input("Enter your target role: ")

print("\nGenerating interview questions for:", role)

questions = {
    "software engineer": [
        "What is OOP?",
        "Explain difference between list and tuple.",
        "What is inheritance?"
    ],

    "data analyst": [
        "What is data cleaning?",
        "Explain SQL joins.",
        "What is data visualization?"
    ],

    "machine learning engineer": [
        "What is overfitting?",
        "Explain supervised learning.",
        "What is a neural network?"
    ]
}

role = role.lower()

if role in questions:
    print("\nInterview Questions:\n")

    for q in questions[role]:
        print("-", q)

else:
    print("\nRole not found.")
