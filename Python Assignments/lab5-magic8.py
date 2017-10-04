'''
lab 5, a magic 8 ball, for all your probing questions!
'''

import random #Zia! remember to import random!!

answers = ['Looking good for you, cuite!', 'Sorry, try again tomorrow.', 'What is it worth to you?', 'If you make it worth my while.',
 'Yes, but only if it is raining.', 'Absolutely!', 'Tragically no. I\'m sad about it, too.', 'Not this time. Make a sacrifice to your gods and ask again.']

question = input('Welcome, supplicant. What is your question? \n')
answer = random.choice(answers) #if you forget to import random, then this part doesn't work.
print(answer)

response = '' #setting an empty variable, so it can be whatever I need?
while response != 'done':
    response = input('What is your next question? \n')
    answer = random.choice(answers) #this also doesn't work if you don't import random

    if response != 'done':
        print(answer)

print('Go forth, brave one, armed with your new knowledge!')