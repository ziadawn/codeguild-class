'''
Lab 23: Blackjack I

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.

First, ask the user for three playing cards. Save the user's inputs as a string: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.

Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10.
At this point, assume aces are worth 1.

Now, in Blackjack, aces can be worth 11 if they won't put the total point value of both cards over 21.

Lastly, figure out what the playing advice will be. Use the following rules:

Less than 17, advise to "Hit"
Over or equal to 17, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Then print out the current total point value and the advice.


'''


def value_full_hand(fh):    # fh is a placeholder variable
    value_full_hand = []
    for i in fh:            # be sure to use the same variable from above
        if i == 'k' or i == 'q' or i == 'j':
            i = 10
            value_full_hand.append(i)
        elif i == 'a':
            i = 1
            value_full_hand.append(i)
        else:
            i = int(i)
            value_full_hand.append(i)
    return sum(value_full_hand)

def play_advice(vfh):
    if vfh < 17:
        return f'{vfh} - Hit'         # f string is another way to join ints and strs more cleanly
    if vfh >= 17 and vfh < 21:
        return f'{vfh} - Stay'
    if vfh == 21:
        return f'{vfh} - Blackjack!'
    if vfh > 21:
        return f'{vfh} - Already busted.'

hand = 0
full_hand = []

while hand < 3:
    cards = input('What is your card? ')
    full_hand.append(cards)
    hand += 1

print(play_advice(value_full_hand(full_hand)))


'''
Variation: 
make options so A can be 1 or 11

make computer give you a random card, advise hit or stay, user can choose, calcuate from there
in other words, I can make you actually play blackjack with the computer!
'''