



class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.point=0
        self.question_list = question_list

    def next_question(self):
        current_question = (self.question_list[self.question_number]).text
        current_answer = (self.question_list[self.question_number]).answer
        user_input  = input(f"Q{self.question_number+1}: {current_question}(True/False): ").lower()
        if user_input == "end":
            print(f"final score is {self.point}/{self.question_number}")
        elif user_input == current_answer.lower():
            self.point+=1
            self.question_number+=1
            print(f"correct - {self.point}/{self.question_number}")
        else: 
            self.question_number+=1
            print(f"wrong {self.point}/{self.question_number}")
        return user_input

    



        
