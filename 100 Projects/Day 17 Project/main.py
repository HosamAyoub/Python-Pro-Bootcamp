from question_model import Question
from data import question_data

question_bank = []

for key in question_data:
    question_bank.append(Question(key['text'], key['answer']))
print(question_bank)