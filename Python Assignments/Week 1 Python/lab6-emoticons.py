'''
Lab 6, a random generator to make emoticons from a set list of eyes, noses, and mouths

Other ideas to try?
Can I have optional hats or things that only sometimes show up?
Another variation: computer asks which ones I like, and stores them. Then I can choose from previously chosen ones or new, random ones?
Can I have the computer not use rejected ones again?
'''

import random #remember to do this!

eyes = [':', ';', '8', 'B', '=']
noses = [' ', 'o', '-', '+']
mouths = [')', '(', 'D', '*', 'P', '|']



i = 0
while i < 5:
    #these are inside the while loop so I get five different emoticons, rather than five of the same, which happened before
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)

    emoticon = eye + nose + mouth

    print(emoticon)
    i = i + 1 #add this so that it does not give me an infinite list of emoticons


