from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for d in question_data:
    question_bank.append(Question(d["text"], d["answer"]))

print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()
