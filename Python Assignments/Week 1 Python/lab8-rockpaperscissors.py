'''
Lab 8, a grand battle of rock paper scissors

Variation to add:
a rechallenge if the computer loses. That will probably invovle while loops.
'''

import random

user_answer = input("Hello mortal! I challenge you to a duel. Rock, paper, or scissors? ") #the computer is snarky

computer_answers = ['rock', 'paper', 'scissors'] #this is a defined list
computer_answer = random.choice(computer_answers) #pulling randomly from list above

if computer_answer == user_answer: #use == to make it true
    print ('It\'s a tie!')
elif computer_answer == 'scissors' and user_answer == 'paper': #these answers must be in quotes because they are strings
    print ('Computer chose scissors. Haha, fleshy human. You lost to me."!')
elif computer_answer == 'rock' and user_answer == 'scissors':
    print('Computer chose rock. You lose! Your meat brain is no match for my digital genius!')
elif computer_answer == 'paper' and user_answer == 'rock':
    print('Computer chose paper. Did you really think you would triumph in this feat of skill? You lose!')
elif computer_answer == 'scissors' and user_answer == 'rock':
    print('Computer chose scissors. You got lucky this time, human.')
elif computer_answer == 'rock' and user_answer == 'paper':
    print('Computer chose rock. Surely your victory is a fluke, not skill.')
elif computer_answer == 'paper' and user_answer == 'scissors':
    print('Computer chose paper. I never lose. I either win or I learn.')