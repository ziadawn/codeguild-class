'''
Lab 13: Guess the Number

Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10.
The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Using a while loop, allow the user to guess 10 times.
If they fail to guess the number after 10 tries, the user is told they've lost.
If the user guesses the number, the user is told they've won and the game exits.
You can get a random number using random.randint:

import random
x = random.randint(1,10)
print(x)

'''

#version 1

import random
x = random.randint(1,10)

guess = input('guess the number! ')
guess = int(guess)  #converted to int so computer can compare the numbers.

i = 0
while guess != x and i < 11:
    guess = input('incorrect. guess again! ')
    guess = int(guess)  #had to remember to do this here, too!
    i = i + 1

if guess == x:
    print('good job! you got it right in ' + str(i) + ' guesses!')  #using i to track guesses is what I insert here
else:
    print('you lose. goodbye!') #put this AFTER the you-win clause, so if you guess on last guess you still win


