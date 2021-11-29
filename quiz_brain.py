


class QuizBrain:
    score=0
    def __init__(self,qList=[]):
        self.number=0
        self.listOfQuestions=qList
    
    def getQuestions(self):
        newQuestion=self.listOfQuestions[self.number]
        self.number+=1
        answer=input(f"Q.{self.number}:{newQuestion.text} (True/False)?")
        if(answer==newQuestion.answer):
            self.score+=1
        print(f"{self.score}/{self.number}")
        if (self.number - self.score) == 3:
            print("You guessed wrong too much")
            exit(0) 