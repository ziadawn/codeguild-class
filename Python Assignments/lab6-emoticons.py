'''
Working on version 2. Right now it doesn't do 5 random emoticons, though it does do 5 and stop. Will poke at later.

Version 2

Use a while loop to generate 5 emoticons.
'''

import random

eyes = [':', ';', '8', 'B', '=']
noses = [' ', 'o', '-', '+']
mouths = [')', '(', 'D', '*', 'P', '|']

eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)

emoticon = eye + nose + mouth

i = 0
while i < 6:
    print(emoticon)
    i = i + 1


