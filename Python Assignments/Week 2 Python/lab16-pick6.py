'''
Lab 16: Pick6

Have the computer play pick6 many times and determine net balance.
Calculate your net winnings (the sum of all expenses and earnings).

Version 2

The ROI (return on investment) is defined as (earnings - expenses)/expenses.
Calculate your ROI, print it out along with your earnings and expenses.
'''


import random
balance = 0

def get_ticket():       # did I actually write a real function here? Yes! Yay!
    ticket = []
    for i in range(6):
        num = random.randint(1, 99)
        ticket.append(num)
    return ticket

pick6 = get_ticket()

print(pick6)

start = input('Are you ready to play? Hit any key to start playing!')

game_play = 0
while game_play < 1000:       # this is the loop of game play. Low number to test.
    ticket = get_ticket()
    balance = balance - 2
    count = 0

    for i in range(len(pick6)):
        if pick6[i] == ticket[i]:
            count += 1

    if count == 0:
        pass
    elif count == 1:
        balance += 4
    elif count == 2:
        balance += 7
    elif count == 3:
        balance += 100
    elif count == 4:
        balance += 50,000
    elif count == 5:
        balance += 1,000,000
    elif count == 6:
        balance += 25,000,000

    game_play += 1


print('After running the numbers 1000 times, your balance is $' + str(balance))





'''
This is where I started, which isn't what I needed but I'm keeping for record of my process:

# all this does is print numbers 1-99, so I didn't have to type them out.
# Probably spent longer on this than it would have taken to just type them out.
# Do I even need them written out for this lab?
# As I work on the next part it occurs to me that I DON'T need this, cause I have those upper/lower bound things. Wheeee. Learning!


# i = 0
# lotto = ''
# while i < 99:
#     i += 1
#     lotto += ', ' + str(i)   # cannot append a string, which is why it didn't work before.
# print(lotto)

Secondary attempt:
pick6 = []              # set at list not string so elements are already individual, manipulatable components
for i in range(6):      # this is shorter/neater than i += 1 etc etc, good for short ranges of numbers
    num = random.randint(1, 99)    # at first was trying random.choice which doesn't work, cause numbers are ints not str
    pick6.append(num)

print(pick6)

start = input('Are you ready to play? Hit any key to start playing!')

# ticket = []
# for i in range(6):
#     num = random.randint(1, 99)
#     ticket.append(num)
#
# print(ticket)

def play_pick6():       # did I actually write a real function here?
    ticket = []
    for i in range(6):
        num = random.randint(1, 99)
        ticket.append(num)
    return ticket

print(play_pick6())

game_play = 0
while game_play < 1000:

    # run play_pick6
    # decrease $ by 2
    # compare each round of game to pick6
        # index must match exactly
    # if match, increase money
    # run again


# def common_elements(list1, list2):
#     return(list1 & list2)
#
# print(common_elements(pick6 & ticket))
'''