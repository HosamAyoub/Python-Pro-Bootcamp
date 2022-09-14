from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    question_bank.append(Question(key['text'], key['answer']))


quiz = QuizBrain(question_bank)
quiz.next_question()