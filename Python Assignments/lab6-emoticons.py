'''
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)

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


