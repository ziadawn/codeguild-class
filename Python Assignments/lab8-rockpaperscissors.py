

import random

user_answer = input("Rock, paper, or scissors? ")

computer_answers = ['rock', 'paper', 'scissors']
computer_answer = random.choice(computer_answers)

if computer_answer == user_answer:
    print ('It\'s a tie!')
elif computer_answer == 'scissors' and user_answer == 'paper':
    print ('Computer chose scissors. You lose!')
elif computer_answer == 'rock' and user_answer == 'scissors':
    print('Computer chose rock. You lose!')
elif computer_answer == 'paper' and user_answer == 'rock':
    print('Computer chose paper. You lose!')
elif computer_answer == 'scissors' and user_answer == 'rock':
    print('Computer chose scissors. Congratulations, you win!')
elif computer_answer == 'rock' and user_answer == 'paper':
    print('Computer chose rock. Congratulations, you win!')
elif computer_answer == 'paper' and user_answer == 'scissors':
    print('Computer chose paper. Congratulations, you win!')