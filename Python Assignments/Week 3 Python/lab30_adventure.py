import random
from os import system

width = 10  # the width of the board
height = 10  # the height of the board


board = []  # create a board with the given width and height. we'll use a list of list to represent the board. start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

player_i = 4 # define the player position
player_j = 4

for i in range(0):           # add 4 enemies in random locations
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

for i in range(10):         # treasure
    treasure_i = random.randint(0, height - 1)
    treasure_j = random.randint(0, width - 1)
    board[treasure_i][treasure_j] = '☆'


print('''
----------------------------------------------------------------------------
Welcome!

For your quest, you must collect all the treasure.

On your way you may encounter hidden enemies, with whom you will do glorious battle.

You may also discover hidden treasure or other things to aid you on your quest.

Collect all the treasure before your enemies defeat you!

Good luck!
---------------------------------------------------------------------------
''')

# print(board[])

# loop until the user says 'done' or dies

treasure = 10   # how much treasure is on the board
hoard = 0       # how much treasure you start with
health = 10     # how much health you start with

while True:

    command = input('Which way would you like to go? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player_j -= 1  # move left
    elif command == 'right':
        player_j += 1  # move right
    elif command == 'up':
        player_i -= 1  # move up
    elif command == 'down':
        player_i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break

    if board[player_i][player_j] == '☆':
        treasure -= 1
        hoard += 1
        if treasure > 0:
            print('Your hoard has increased!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print(f'+++++++++++++++++++++++++++++++++'
                  'Congratulations, you\'ve collected all the treasure! You win! \n'
                  'Your final stats: health {health} and treasure hoard {hoard}. Well done!\n'
                  '+++++++++++++++++++++++++++++++++')  # could ask if want to play again?
            break

    # system('clear')
    for i in range(height):             # print out the board
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            elif board[i][j] == '§':
                print(' ', end=' ')     # invisible enemy!
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

    # board(clear)


# ♡
# ϟ ☼ ☽ ☄ ☃ ❋ ✣ ❀ ❊ ✽ ✾ ✣ ✤ ❁ ✚ ☩ ♢ ⌂ ◎ ○ ◊ ◯