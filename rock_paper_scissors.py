import random

player_wins = 0
computer_wins = 0
winning_score = 2 # this can be set to whatever you want


while player_wins < winning_score and computer_wins < winning_score:
    
    print(f'Player score: {player_wins} Computer score: {computer_wins}')
    print('Rock...\nPaper...\nScissors...')
    player = input('Player, choose your move: ').lower()
    computer = ''
    
    if player == 'quit' or player == 'q':
        break

    rand_num = random.randint(0,2)
    
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    elif rand_num == 2:
        computer = 'scissors'

    print(f'Computer plays {computer}!')

    if player == computer:
        print("It's a draw! Go again!")
    elif player == 'rock':
        if computer == 'scissors':
            print('You win! + 1 point!')
            player_wins += 1
        else:
            print('Computer wins! + 1 point to the computer!')
            computer_wins += 1
    elif player == 'paper':
        if computer == 'rock':
            print('You win! + 1 point!')
            player_wins += 1 
        else:
            print('Computer wins! + 1 point to the computer!')
            computer_wins += 1
    elif player == 'scissors':
        if computer == 'paper':
            print('You win! + 1 point!')
            player_wins += 1
        else:
            print('Computer wins! + 1 point to the computer!')
            computer_wins += 1 
    else:
        print('Please enter a valid move')
if player_wins > computer_wins:
    print('Congrats! You won!')
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print('Bummer, the computer won... better luck next time')
print(f'FINAL SCORES...\nPlayer score: {player_wins} \nComputer score: {computer_wins}')
