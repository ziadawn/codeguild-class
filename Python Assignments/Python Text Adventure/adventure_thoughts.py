'''
visible treasure: collect treasure

invisible enemies: do battle (how?) rock paper scissors
    if lose: lose health or treasure
    if win: defeat enemy, gain random treasure?
    if tie: display enemy, get half treasure


invisible health bonus

invisible bonus treasure





collect all visible treasure to win
lose if all health gone

'''


from world import World
from entities import Player, Knight
from items import Treasure

world = World(15, 15)

player_i, player_j = world.random_location()
player = Player(player_i, player_j)
world.entities.append(player)

for i in range(10):
    knight_i, knight_j = world.random_location()
    knight = Knight(knight_i, knight_j)
    world.entities.append(knight)

for j in range(10):
    treasure_i, treasure_j = world.random_location()
    treasure = Treasure(treasure_i, treasure_j)
    world.entities.append(treasure)

while True:
    world.draw()
    command = input('what is your command? ').lower()
    if command in ['done', 'quit', 'exit']:
        break
    if command in ['left', 'a']:
        if player.loc_i > 0:        # this keeps player from going off the edge of the board
            player.loc_i -= 1
    elif command in ['right', 'd']:
        player.loc_i += 1
    elif command in ['up', 'w']:
        player.loc_j -= 1
    elif command in ['down', 's']:
        player.loc_j += 1
    else:
        print('command not recognized')

    for thing in world.entities:
        if (thing.loc_i, thing.loc_j) == (player.loc_i, player.loc_j):
            if type(thing) is type(knight):
                print("knight")
                #call fight function

            elif type(thing) is type(treasure):
                print("you have found treasure!")
                player.inventory.append(1)
                world.entities.remove(thing)
                print(player.inventory())



# '''
# if board[player_i][player_j] == '☆':
#     treasure -= 1
#     hoard += 1
#     if treasure > 0:
#         print('Your hoard has increased!')
#         board[player_i][player_j] = ' '  # remove the enemy from the board
#     else:
#         print('''
#             f'+++++++++++++++++++++++++++++++++'
#               'Congratulations, you\'ve collected all the treasure! You win! \n'
#               'Your final stats: health {health} and treasure hoard {hoard}. Well done!\n'
#               '+++++++++++++++++++++++++++++++++'
#               ''')  # could ask if want to play again?
#         break
# '''
#