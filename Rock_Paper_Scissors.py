# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a
# message of congratulations to the winner, and ask if the players want
# to start a new game)

p1 = input('Who is player 1?: ')  # player 1 name
p2 = input('Who is player 2?: ')  # player 2 name
game_rules = 0  # variable definition
while game_rules != 1:  # condition allowing loop to run being that 1 is not = 0 which is true
    p1_choose = input(p1 + ' choose rock, paper, or scissors: ')  # variable for player 1's move
    p2_choose = input(p2 + ' choose rock, paper, or scissors: ')  # variable for player 2's move
    rock = 'rock'  # rock defined
    paper = 'paper'  # paper defined
    scissors = 'scissors'  # scissors defined
    yes = 'yes'  # yes defined
    no = 'no'  # no defined
    if p1_choose == rock and p2_choose == scissors:  # rock > scissors
        print('Congrats ' + p1)
    elif p2_choose == rock and p1_choose == scissors:  # rock > scissors
        print('Congrats '+p2)
    elif p1_choose == scissors and p2_choose == paper:  # scissors > paper
        print('Congrats ' + p1)
    elif p2_choose == scissors and p1_choose == paper:  # scissors > paper
        print('Congrats ' + p2)
    elif p1_choose == paper and p2_choose == rock:  # paper > rock
        print('Congrats ' + p1)
    elif p2_choose == paper and p1_choose == rock:  # paper > rock
        print('Congrats ' + p2)
    elif (p1_choose != rock and p1_choose != paper and p1_choose != scissors) or (p2_choose != rock and p2_choose !=
                                                                    paper and p2_choose != scissors):  # error message
        print('Invalid choice, go again')
    elif (p1_choose == rock and p2_choose == rock) or (p1_choose == paper and p2_choose == paper) or (p1_choose ==
    scissors and p2_choose == scissors):
        print("It's a tie, go again")
    choice_restart = (input('Do you want to restart game?: '))  # variable defined
    if choice_restart == yes:  # when player wants to restart
        continue
    elif choice_restart != yes and choice_restart != no:  # error message
        print('Invalid choice')
    else:  # when player does not want to restart
        break




