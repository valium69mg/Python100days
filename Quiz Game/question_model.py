#QUESTION MODEL MODULE
import random

question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class question():
    
    def __init__(self): # Picks random question from line 4 list
        self.text = ""
        self.answer = ""

    def setQuestion(self):
        question_list_length = len(question_data)
        rand_index = random.randint(0,question_list_length-1)
        dict = question_data[rand_index]
        self.text = dict["text"]
        self.answer = dict["answer"]
    
    def getQuestion(self):
        return self.text

    def getAnswer(self):
        return self.answer
    
    
   
        

