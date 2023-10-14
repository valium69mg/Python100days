# QUIZ GAME BRAIN

class quizBrain():
    
    def __init__(self,random_question,random_answer):
        self.question = random_question
        self.answer = random_answer
        self.choosenAnswer = ""
    
    
    def setChoosenAnswer(self,answer_given: str):
        self.choosenAnswer = answer_given
    
    def evaluateAnswer(self):
        if self.answer == self.choosenAnswer:
            return True
        return False