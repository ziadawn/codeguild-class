'''
lab 2, write a madlib

'''


adjective = input('give me an adjective related to size: ')
noun_1 = input('give me an thing or object: ')
thinking = input('give me a synonym for thinking: ')
position = input('give me a relative position, such as under or beside: ')
noun_2 = input('give me a noun: ')
noun_3 = input('give me another noun: ')
noun_4 = input('give me one more noun: ')

#I've considered just asking for four nouns at once and then slotting them in, but moved on to another lab

reply = 'twinkle twinkle ' + adjective + ' ' + noun_1 + '\nhow I ' + thinking + ' what you are. \n' \
        + position + ' the ' + noun_2 + ' so high, \nlike a ' + noun_3 + ' in the ' + noun_4 + '.'

print(reply)


'''
I have the original here so I could decide which words to replace

twinkle twinkle [little] [star]
how i [wonder] what you are
[up above] the [world] so high
like a [diamond] in the [sky]
'''