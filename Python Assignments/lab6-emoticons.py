'''
Version 3, next thing to try! Can I have optional hats or things that only sometimes show up?
'''

import random

eyes = [':', ';', '8', 'B', '=']
noses = [' ', 'o', '-', '+']
mouths = [')', '(', 'D', '*', 'P', '|']



i = 0
while i < 5:
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)

    emoticon = eye + nose + mouth

    print(emoticon)
    i = i + 1


