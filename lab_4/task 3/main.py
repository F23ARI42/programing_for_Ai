from q_model import Question
from data import question_data
question_bank = [Question(q["text"], q["answer"]) for q in question_data ]
for question in question_bank:
    print(question)