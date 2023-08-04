import random

# Quiz questions and answers
questions = [
    {
        "question": "What is Django?",
        "options": ["A. A web development framework", "B. An operating system", "C.  A database management system"],
        "answer": "A"
    },
    {
        "question": "What programming language is Django primarily based on?",
        "options": ["A. Java", "B. Python", "C. C++"],
        "answer": "B"
    },
    {
        "question": "Django follows the Model-View-Controller (MVC) architectural pattern.",
        "options": ["A. XML", "B. HTML and CSS", "C. JavaScript "],
        "answer": "B"
    },
    {
        "question": "Which of the following is NOT a Django template engine?",
        "options": ["A. Mako", "B. Django Templates", "C. React "],
        "answer": "C"
    },
]

def ask_question(question_obj):
    print(question_obj["question"])
    for option in question_obj["options"]:
        print(option)
    user_answer = input("Your answer (enter A, B, or C): ").upper()
    return user_answer

def run_quiz():
    score = 0
    random.shuffle(questions)

    for question in questions:
        user_answer = ask_question(question)
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    total_questions = len(questions)
    print(f"You scored {score}/{total_questions} in the quiz.")

if __name__ == "__main__":
    print("Welcome to the Quiz App!")
    run_quiz()
