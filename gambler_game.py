# Simulates a gambler who start with $stake and place fair $1 bets until
# he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
# times he/she wins and the number of bets he/she makes. Run the experiment N
# times, averages the results, and prints them out.

import random


def play_game(_stake, _goal, _no_of_times):
    count_bet = 0
    win = 0
    loss = 0

    for i in range(no_of_times):
        count_bet += 1
        if random.randint(0, 1) == 1:
            _stake += 1
        else:
            _stake -= 1
        if _stake == _goal:
            win += 1
        else:
            loss += 1
    print("the number of wins : ", win)
    print("the number of loss : ", loss)
    print("the number of times the game is played to reach the goal : ", count_bet)
    win_percent = win/count_bet * 100
    loss_percent = loss/count_bet * 100
    print("the win percent is : ", win_percent)
    print("the loss percent is : ", loss_percent)


stake = int(input("enter the initial stake you want to place : "))
goal = int(input("enter the goal value : "))
no_of_times = int(input("enter how many times you want to try : "))

# calling a functions
play_game(stake, goal, no_of_times)

