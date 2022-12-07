# The following is the game rules
# Rock = A, 1 point
# Paper = B, 2 point
# Scissors =C, 3 point
# Loose = 0 = X
# draw = 3 = Y
# win = 6 = Z
try:
    #read txt file and store it in fr
    fr = open("Tournament.txt",'r')
    gamePlan = fr.readlines()
    #list will be used to store each line of the txt file
    listgamePlan = []
    #default values for better code readability
    win = 6
    draw = 3
    loose = 0
    rock = 1
    paper = 2
    scissors = 3
    #scores will be used to hold the totl amount of scores
    scores = 0

    #for loop to store each line into the list
    for round in gamePlan:
        listgamePlan.append(round)
    
    #filters each character in of the previous list
    lis=[list(x) for x in listgamePlan]

    #for loop with the algoithym suggested by the Elf
    for round in lis:
        if round[0] == 'A' and round[2] == 'X':
            scores += loose + scissors
        elif round[0] == 'A' and round[2] == 'Y':
            scores += draw + rock
        elif round[0] == 'A' and round[2] == 'Z':
            scores += win + paper
        elif round[0] == 'B' and round[2] == 'X':
            scores += loose + rock
        elif round[0] == 'B' and round[2] == 'Y':
            scores += draw + paper
        elif round[0] == 'B' and round[2] == 'Z':
            scores += win + scissors
        elif round[0] == 'C' and round[2] == 'X':
            scores += loose + paper
        elif round[0] == 'C' and round[2] == 'Y':
            scores += draw + scissors
        elif round[0] == 'C' and round[2] == 'Z':
            scores += win + rock
    #print total scores
    print(scores)
finally:
    fr.close()
