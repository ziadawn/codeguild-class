'''
Lab 13: Guess the Number

Version 2

Allow the user to make an unlimited number of guesses using a while True and break.
Keep track of how many guesses the user has made, and tell them at the end.

Version 3

Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
'''


import random
x = random.randint(1,20)

while True:
    guess = input('guess the number: ')
    guess = int(guess)
    if guess > x:
        print('you guessed too high')
    elif guess < x:
        print('you guessed too low')
    elif guess == x:
        print('yay!')
        break



'''
way simpler version! 
while True and break means I don't have to have all the cumbersome variable that I did in version 1 
the downside is that I can't make different optsions of replies, as I did in version 1. 
So choose depending on what your goals are!

here's version 1, for ref

guess = input('guess the number! ')
guess = int(guess)  #converted to int so computer can compare the numbers.

i = 0
while guess != x:
    guess = input('incorrect. guess again! ')
    guess = int(guess)  #had to remember to do this here, too!
    i = i + 1

if guess == x:
    print('good job! you got it right in ' + str(i) + ' guesses!')  #using i to track guesses is what I insert here

'''