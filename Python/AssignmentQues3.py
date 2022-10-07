

#3. . Create a program to play RPS Game

'''Inputs:
1. Enter Player name 1
2. Enter Player name 2
3. Enter Player 1 Choice
4. Enter Player 2 Choice


Choices are "Rock", "Scissor", "Paper"

result: who wins?


display result: Player name with choice Rock wins
Player name with choice Scissor Lose


how to manipulate result:
If P1 enter Rock and P2 enters Scissor then P1 Wins
if P1 enter Rock and P2 enters Paper then P2 Wins
if P1 enter Scissor and P2 enters Paper then P1 wins
if both player enters the same choice it should say "Tie"

'''
name1 = input("enter player name 1")
name2 = input("enter player name 2")

print("""Enter any of the following choices
          1) Rock
          2) Scissor
          3) Paper
          \n""")

choice1 = input("enter player1 choice")
choice2 = input("enter player 2 choice")

if (choice1=="Rock" and choice2=="Scissor"):
    print("name1 wins")

elif (choice1=="Rock" and choice2=="Paper"): 
    print("name2 wins")

elif (choice1=="Scissor" and choice2=="paper"):
    print("name1 wins")

elif (choice1=="Scissor" and choice2=="Rock"):
    print("name2 wins")

elif (choice1=="Paper" and choice2=="Scissor"):
    print("name2 wins")

elif (choice1=="Paper" and choice2=="Rock"):
    print("name1 wins")

else:
    print("Tie")









