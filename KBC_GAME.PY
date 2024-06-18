#KBC
# Importing the random module to shuffle questions
import random

prize_money=0

#questions and answers 

questions =[{
    "question" :" Which state in India is also known as 'Dev Bhoomi' ?",
    "option" : ["A. Uttarakhand","B. Rajasthan" ,"C.Himachal Pradesh","D.Arunachal Pradesh"],
    "answer":  "A"},

  {  "question" :" Which Indian Cricketer has the record for scoring the most number of ODI centuries?",
    "option" : ["A. Sachin Tendulkar","B. Virat Kohli","C. Rohit Sharma","D. Rahul Dravid"],
    "answer":  "B"},

   { "question" : " What is the name of the famous poet who wrote India's national anthem “Jana Gana Mana”?" ,
    "option" : ["A. Bankim Chandra Chattopadhyay","B. Rabindranath Tagore","C. Muhammad Iqbal","D.  Sarojini Naidu"] ,
    "answer" :  "B"},

   {"question": "The first ever full-length Gujarati movie is based on the life of which of the following personalities?",
   "option" : ["A. Narsi Mehta", "B. Premchand Bhatt","C. Mahatma Gandhi","D. Mira Bai"],
     "answer":  "A"},

   { "question":  " Which of the following Prime ministers of India was born in present-day Gujarat? ",
    "option" :["A. Chaudhary Charan Singh","B. Gulzarilal Nanda","C. Morarji Desai","D. Jawaharlal Nehru"],
    "answer":  "C"},

   { "question" :"Who is the author of the famous book “The God of Small Things”? ",
    "option" :["A. R.K. Narayan","B. Salman Rushdie","C. Jhumpa Lahiri","D. Arundhati Roy"],
    "answer":  "D"}]

# Shuffle the questions
random.shuffle(questions)
for question in questions:
    print(question["question"])
    for option in question["option"]:
      print(option)

    user_answer = str(input("Enter your answer (option number): "))

    if user_answer == question["answer"]:
      print("Correct answer!")
      prize_money += 10000
    else:
        print("Wrong answer!")
        break 
print("Prize Money:", prize_money)
 
