# create dictionary that stores questions and answers
quiz = {
    "question_1": {
        "question": "What is the capital of France",
        "answer": "Paris"
    },
    "question_2": {
        "question": "What is the capital of Nigeria",
        "answer": "Abuja"
    },
    "question_3": {
        "question": "What is the capital of Germany",
        "answer": "Berlin"
    },
    "question_4": {
        "question": "What is the capital of Italy",
        "answer": "Rome"
    },
    "question_5": {
        "question": "What is the capital of Ghana",
        "answer": "Accra"
    },
    "question_6": {
        "question": "What is the capital of Togo",
        "answer": "Lome"
    },
    "question_7": {
        "question": "What is the capital of Japan",
        "answer": "Tokyo"
    }
}

# declare a variable that tracks score of user
score = 0

# loop through dictionary
for key, value in quiz.items():
    # display each question to the user and allow them answer
    print(value['question'])
    answer = input("Enter Answer: ")

    # show user if they are right or wrong
    if answer.lower() == value['answer'].lower():
        print("Correct")
        score += 1
        print(f"Your score is {score}\n")
    else:
        print("Incorrect")
        correct = value['answer']
        print(f"The answer is {correct}")
        print(f"Your score is {score}\n")

# show final result when quiz is completed
