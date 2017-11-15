# can make enemy attack back
# you win if all enemies are gone
# can make health resoration
# can make map  -- nothing to see until you find it
# DONE - can ask player how difficult they want to be!
# can have hidden AND visible enemies
# rock paper scissors to do battle?
# hidden treasure! if find hidden map, could reveal treasure?
# could we buy off enemies?

## need to loop so if you loose rps you try again or run away
## when game over, print final health and treasure scores
## currently you can move off the board, that's no good!

import random

difficulty = input('how many enemies would you like to face? ')
difficulty = int(difficulty)

player_treasure = 0
rps = ['rock', 'paper', 'scissors']
health = 10

width = 10
height = 10
board = []
for i in range(height):
    board.append([])
    for j in range(width):
        board[i].append(' ')

player_i = 1
player_j = 0

for i in range(difficulty):  # this number is how many enemies there will be
    enemy_i = random.randint(0, height-1)
    enemy_j = random.randint(0, width-1)
    board[enemy_i][enemy_j] = '₰'

treasures = []
for i in range(difficulty // 2):  # this number is how much treasure there will be
    treasure_i = random.randint(0, height-1)
    treasure_j = random.randint(0, width-1)
    # board[treasure_i][treasure_j] = 'ꕥ'
    #board_treasure = board[treasure_i][treasure_j]
    treasures.append([treasure_i, treasure_j])

#treasures = [[0,0],[7,8]] --- just used to test that I was finding hidden treasure

while True:

    for i in range(height):
        for j in range(width):
            if i == player_i and j == player_j:
                print('☆', end=' ')
            else:
                print(board[i][j], end=' ')
        print()

    command = input('which way shall you travel? ')

    if command == 'done':
        break
    elif command == 'left':
        player_j -= 1
    elif command == 'right':
        player_j += 1
    elif command == 'up':
        player_i -= 1
    elif command == 'down':
        player_i += 1


    for treasure in treasures:
        if player_i == treasure[0] and player_j == treasure[1]:
            print('you found treasure!')

    if player_i == treasure_i and player_j == treasure_j:
        print('you found treasure!')
        board[player_i][player_j] = ' '     #removes treasure from the board
        player_treasure += 1        #are these variables matching up right now?
        board_treasure -= 1

    if board[player_i][player_j] == '₰':
        print('you\'ve encountered an enemy! now you must do battle.')

        player_choice = input('rock, paper, or scissors? ')
        print('player choice: ' + player_choice)

        enemy_chioce = random.choice(rps)
        print('enemy choice: ' + enemy_chioce)

        if player_choice == enemy_chioce:
            print('tie! your former enemy has gifted you treasure, out of respect')
            player_treasure += 2
        elif player_choice == 'rock' and enemy_chioce == 'scissors':
            print('player wins!')
        elif player_choice == 'paper' and enemy_chioce == 'rock':
            print('player wins!')
        elif player_choice == 'scissors' and enemy_chioce == 'paper':
            print('player wins!')

        board[player_i][player_j] = ' '     #removes an enemy from the board
        difficulty -= 1
        if difficulty == 0:
                print('you have defeated all the enemies, you win! yay!')
                print('final health: ' + str(health))
                print('final treasure: ' + str(player_treasure))
                break

        elif player_choice == 'rock' and enemy_chioce == 'paper':
            print('enemy wins!')
        elif player_choice == 'paper' and enemy_chioce == 'scissors':
            print('enemy wins!')
        elif player_choice == 'scissors' and enemy_chioce == 'rock':
            print('enemy wins!')

        health -= 1
        if health == 0:
                print('your health has run out and you have perished. you lose.')
                print('final health: ' + str(health))
                print('final treasure: ' + str(player_treasure))
                break




'''
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '     #removes an enemy from the board
            difficulty -= 1
            if difficulty == 0:
                print('you have defeated all the enemies, you win! yay!')
                break
        else:
            print('you hestitated and were slain')
            break
'''
*