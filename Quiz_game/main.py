from question_model import Question
from quiz_brain import QuizBrain
from data import category_name,question_data

question_bank =[]
for q_and_a in question_data:
    question =q_and_a['question']
    answer = q_and_a['correct_answer'].lower()
    new_q = Question(question,answer)
    question_bank.append(new_q)


quiz1 = QuizBrain(question_bank)
user_choice = ""
print(f"Questions are from {category_name}")
for x in question_bank:
    if user_choice != "end":
        user_choice = quiz1.next_question()
    else:
        exit()