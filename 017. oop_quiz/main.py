from data import question_data
from question_model import Question

question_bank = []

for d in question_data:
    question_bank.append(Question(d["text"], d["answer"]))

print(question_bank)
