data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]



def question(data):
    correct = 0
    incorrect = 0
    wrong_answers = []

    for index, question in enumerate(data):
        user_answer = input(question['question']).strip()
        if user_answer.lower() == question['answer'].lower():
            print("Correct!\n")
            correct += 1
        else:
            print("Wrong!\n")
            incorrect += 1
            wrong_answers.append({"question" : question['question'], "your_answer" : user_answer, "correct_answer" : question['answer']})
    return correct, incorrect, wrong_answers

def show_result(correct, incorrect, wrong_answers):
    print("======================================================")
    print(f"You have {correct} correct answers and {incorrect} incorrect answers.\n")

    if wrong_answers:
        for mistake in wrong_answers:
            print(f"{mistake['question']}")
            print(f"Your answer : {mistake['your_answer']}")
            print(f"Correct answer : {mistake['correct_answer']}")
            print("-------------------------------")

    if incorrect > 3:
        play_again = input("Do you want to play again ? (Y)es, (N)o : ")
        if play_again.upper() == "Y":
            correct, incorrect, wrong_answers = question(data)
            show_result(correct, incorrect, wrong_answers)
        else:
            print("Thanks for playing! Bye!")


correct, incorrect, wrong_answers = question(data)
show_result(correct, incorrect, wrong_answers)
