from data import question_data
from question_model import Question
from quiz_brain import Quiz
import time
my_time = 5

question_bank = []
for q in question_data:
     question_text = q["question"]
     question_answer = q["answer"]
     new_question = Question(question_text, question_answer)
     question_bank.append(new_question)
   

quiz = Quiz(question_bank)
while quiz.still_has_question():
   
    for x in range(my_time,0,-1):
        seconds = x % 60
        minutes = int(x/60) % 60
        hours = int(x/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    quiz.next_question() 


print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")    

