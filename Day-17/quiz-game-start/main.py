import question_model
import data
import random

quiz_set_5 = []

while len(quiz_set_5) < 5:
    question = random.choice(data.question_data)
    if question not in quiz_set_5:
        question_object = question_model.Question(question["text"], question["answer"])
        quiz_set_5.append(question_object)


for i in range(0,5):
    print(f"question: {quiz_set_5[i].text} || answer: {quiz_set_5[i].answer}")
