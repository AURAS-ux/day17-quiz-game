from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    newQuestion = Question(question.get("text"),question.get("answer"))
    question_bank.append(newQuestion)

brain = QuizBrain(question_bank)

shouldStop=False
while not shouldStop:
    brain.getQuestions()
    if brain.number==len(question_bank):
        print(f"Game over!Your final score was {brain.score}/{brain.number}")
        shouldStop=True

