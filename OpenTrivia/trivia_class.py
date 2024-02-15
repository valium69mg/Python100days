import requests
import html
import random 

class Trivia:
        
        def __init__(self):
            self.current_question = None
            self.correct_answers = 0
            self.incorrect_answers = 0
            self.questions = None
            self.remaining_questions = None
            self.getQuestions()
        
        def getQuestions(self):
            """
            VARIABLES NEEDED TO MAKE THE GET REQUEST
            """
            endpoint = "https://opentdb.com/api.php"
            trivia_params = {
                "amount":10,
                "type":"boolean"
            }

            response = requests.get(endpoint,params=trivia_params)
            response.raise_for_status()
            list_of_questions = response.json()['results']
            purged_questions = []
            for question in list_of_questions:
                question_text = html.unescape(question['question']) # UNESCAPE THE QUESTION TEXT USING HTML MODULE
                correct_answer = question['correct_answer']
                new_dict = {
                    "question_text":question_text,
                    "correct_answer":correct_answer
                }
                purged_questions.append(new_dict)

            self.questions = purged_questions

            return True
        
        def evalQuestion(self,user_answer: str):
                if (self.current_question != None):
                    if (self.current_question['correct_answer'] == "True"):
                        self.correct_answers += 1 
                        return True    
                    else:
                        self.incorrect_answers += 1
                        return False  
         
        
        def nextQuestion(self):
            if (self.checkGameOver() == False): 
                self.current_question = random.choice(self.questions)
                new_list_of_questions = self.questions
                new_list_of_questions.remove(self.current_question)
                self.questions = new_list_of_questions
                return self.current_question['question_text'] 
            else:
                pass


        def checkGameOver(self):
             if (self.questions == []):
                print(f"Your score is: {self.correct_answers}/{self.correct_answers+self.incorrect_answers}") 
                self.current_question = None
                return True
             else:
                  return False
             

             
