import random

knight_answer_answers = ['rock', 'paper', 'scissors'] #this is a defined list
knight_answer = random.choice(knight_answer) #pulling randomly from list above

def battle():
    knight_win = input('Your opponent has won. Would you like to challenge them again or run away? ')
    player_win = input('You have defeated the knight!')

    if knight_answer == user_answer: #use == to make it true
        return ('It\'s a tie!')

    while True:
        if knight_answer == 'scissors' and user_answer == 'paper':
            return ('Your opponent chose scissors.')
        elif knight_answer == 'rock' and user_answer == 'scissors':
            return('Your opponent chose rock. You lose!')
        elif knight_answer == 'paper' and user_answer == 'rock':
            return('Your opponent chose paper.')

    while True:
        if knight_answer == 'scissors' and user_answer == 'rock':
            return('Computer chose scissors.')
        elif knight_answer == 'rock' and user_answer == 'paper':
            return ('Computer chose rock.')
        elif knight_answer == 'paper' and user_answer == 'scissors':
            return ('Computer chose paper.')

print(battle())

    #
    #
    # if board[player_i][player_j] == '§':
    #     print('You\'ve encountered an enemy! They have challenged you to a grand duel of rock, paper, scissors.')
    #     action = input('Will you do battle or run away? ')
    #     if action == 'battle' or action == 'do battle':
    #
    #
    #
    #         # print('you\'ve slain the enemy')
    #         board[player_i][player_j] = ' '  # remove the enemy from the board
    #     else:
    #         print('you hestitated and were slain')
    #         break