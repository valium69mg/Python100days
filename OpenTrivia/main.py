from tkinter import *
from trivia_class import Trivia
from ui import QuizInterface


quiz = Trivia() #Quiz with 5 questions 
quiz_ui = QuizInterface(quiz)
