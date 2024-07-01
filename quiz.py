
class Quiz:
    def __init__(self,quest,ans):
        self.question=quest
        self.answer=ans
# Quiz1=Quiz('Who is known as father of India? \n a:Gandiji  b:Nehru c:Azad ','a')
# Quiz2=Quiz('Which is the capital city of India? \n a:Goa  b:Kerala c:Delhi ','c')
# Quiz3=Quiz('When is the independence day of India? \n a:Jan 23  b:Nov 13, c:Aug 15 ','c')
# Quiz4=Quiz('Which is the most spoken language of India? \n a:Tamil  b:Malayalam , c:Hindi ','c')
# quiz_objs=[Quiz1,Quiz2,Quiz3,Quiz4]
# score=0
# for quiz in quiz_objs:
#     user_ans=input(quiz.question) 
#     if user_ans==quiz.answer:
#         score+=1
# print(f"quiz finished!!\n your score is {score}/{len(quiz_objs)}")

  
                
                
                 #More neat code#
            #--------------------------#

quiz_list=[
    'Who is known as father of India? \n a:Gandiji  b:Nehru c:Azad ',
    'Which is the capital city of India? \n a:Goa  b:Kerala c:Delhi ',
    'When is the independence day of India? \n a:Jan 23  b:Nov 13, c:Aug 15 ',
    'Which is the most spoken language of India? \n a:Tamil  b:Malayalam , c:Hindi '
]

questions=[
    Quiz(quiz_list[0],'a'),
    Quiz(quiz_list[1],'c'),
    Quiz(quiz_list[2],'c'),
    Quiz(quiz_list[3],'c'),]

def start_quiz(questions):
    score=0
    for quest in questions:
        user_answer=input(quest.question)
        if user_answer==quest.answer:
           score+=1
    print(f"Quiz finished , You got {score} /{len(questions)}")
    
    
    
start_quiz(questions)