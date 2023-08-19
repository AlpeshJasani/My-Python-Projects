import random

def play():
    com_score = user_score = 0
    
    while com_score != 5 and user_score != 5:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors : ")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print("It's a tie")

        # r > s, s > p, p > r
        elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
            or (user == 'p' and computer == 'r'):
            user_score += 1
            print(f'You won!\tScore: Your: {user_score}\t Computer: {com_score}')
        else:
            com_score += 1
            print(f'You lost!\tScore: Your: {user_score}\t Computer: {com_score}')

    if user_score == 5:
        print("\nYaaHoo!! You won the Game!! :)\n")
    else:
        print("\nOpps!! You lose the Game!! :(\n")

play()
