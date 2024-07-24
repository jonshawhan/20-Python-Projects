# Dictionary that stores questions and answers
# Variable that tracks the score of the player
# loop through dictionary using key value pairs
# display each question to user and allow them to answer
# tell if right or wrong
# show final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))

    else:
        print("Wrong")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score) + "\n\n")

print("You got " + str(score) + " out of 7 questions correctly\n")
print("Your percentage is " + str(score/7 * 100) + "%")