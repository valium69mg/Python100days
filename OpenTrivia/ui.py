from tkinter import *
from trivia_class import Trivia

class QuizInterface:

    
    def __init__(self,quiz:Trivia):
        # QUIZ BRAIN VARIABLEs
        self.quiz = quiz
        self.score = 0
        # WINDOW CONFIG
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=300,height=500)
        self.window.config(bg="#201658")
        self.window.config(padx=20,pady=20)
        # SCORE LABEL
        self.score_label = Label(self.window,text="Score: 0",bg="#98ABEE")
        self.score_label.grid(row=1,column=2)
        # BUTTONS 
        self.true_button = Button(self.window,text="True",bg="green",command=self.truePressed)
        self.true_button.grid(row=3,column=1)
        self.false_button = Button(self.window,text="False",bg="red",command=self.falsePressed)
        self.false_button.grid(row=3,column=2)
        # CANVAS
        self.canvas = Canvas(self.window,width=280,height=300,bg="#98ABEE")
        self.canvas_text = self.canvas.create_text(145,145,width=200,text="Welcome to the Quizzler.",font=("Arial",16,"italic"))
        self.canvas.grid(row=2,column=1,columnspan=2,padx=20,pady=10)
        self.getNextQuestion()
        self.window.mainloop()

    def getNextQuestion(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.config(bg="#98ABEE")
        if (self.quiz.checkGameOver() == False):
            question_text = self.quiz.nextQuestion()
            self.canvas.itemconfig(self.canvas_text,text=question_text)
        else:
            question_text = f"GAME OVER.\nScore: {self.score}/10"
            self.canvas.itemconfig(self.canvas_text,text=question_text)

    def truePressed(self):
        answer = self.quiz.evalQuestion("True")
        self.giveFeedback(answer)

    def falsePressed(self):
        answer = self.quiz.evalQuestion("False")
        self.giveFeedback(answer)

    def giveFeedback(self,answer: bool):
        if (answer == True):
            self.canvas.config(bg="green")
            self.score += 1
        else:   
            self.canvas.config(bg="red")
        self.window.after(1000,self.getNextQuestion)