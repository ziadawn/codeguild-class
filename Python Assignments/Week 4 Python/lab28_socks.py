'''
Lab: Socks
V1:
You've just finished laundry and your expansive sock collection is in complete disorder.
Sort your socks into pairs and pull out any loners.
Generate a list of 100 random socks, randomly chosen from a set of types.

V2:
Now you have a mix of types and colors.
Represent socks using tuples containing one color and one type ('black', 'crew').
Randomly generate these, and then group them into pairs.
'''

import random

sock_types = ['ankle', 'crew', 'OTK', 'thigh', 'knee', 'legwarmers']
sock_colors = ['black', 'grey', 'striped', 'purple']
socks = []
for i in range(100):
    type_sock = random.choice(sock_types)
    color_sock = random.choice(sock_colors)
    socks.append((type_sock, color_sock))
print(socks)

happy_socks = {}        # matched socks
lonely_socks = {}       # unmatched socks
while len(socks) > 0:   # while my list of socks is still more than empty, do this!
    match_socks = socks.pop()
    for i in range(len(socks)): # index of socks
        sock = socks[i]         # my sock is at index i
        if sock == match_socks: # the indexed sock is my match_sock, which is removed from the master list above
            socks.pop(i)
            if sock in happy_socks: # if my indexed sock is in my happy socks....
                happy_socks[match_socks] += 1    # I add it to the list as a match...
            else:
                happy_socks[match_socks] = 1
            break
    else:
        if sock in lonely_socks: # if my indexed sock is in my happy socks....
            lonely_socks[match_socks] += 1    # I add it to the list as a match...
        else:
            lonely_socks[match_socks] = 1

print(f'You have the the following pairs of socks: {happy_socks}')      # Would really love to format this printing better
print(f'You have only one of these socks: {lonely_socks}')




