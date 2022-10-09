Rock = '''
 _______
---' ____)
 (_____)
 (_____)
 (____)
---.__(___)
'''

Paper = '''
 _______
---' ____)____
 ______)
 _______)
 _______)
---.__________)
'''

Scissors = '''
 _______
---' ____)____
 ______)
 __________)
 (____)
---.__(___)
'''
import random
game = [Rock, Paper, Scissors]
# Print multiline instruction
# performstring concatenation of string
print("Rules of the Rock paper scissor game as follows: \n"
 +"Rock vs paper->paper wins \n"
 + "Rock vs scissor->Rock wins \n"
 +"paper vs scissor->scissor wins \n")
 
while True:
 print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
 
 # take the input from user
 choice = int(input("User turn: "))
 
 # OR is the short-circuit operator
 # if any one of the condition is true
 # then it return True value
 
 # looping until user enter invalid input
 while choice > 3 or choice < 1:
 choice = int(input("Enter valid input: "))
 
 
 # corresponding to the choice value
 if choice == 1:
 choice_name = 'Rock'
 elif choice == 2:
 choice_name = 'paper'
 else:
 choice_name = 'scissor'
 
 # print user choice 
 print(game[choice-1])
 print("user choice is: " + choice_name)
 print("\nNow its computer turn.......")
 
 # Computer chooses randomly any number 
 # among 1 , 2 and 3. Using randint method
 # of random module
 comp_choice = random.randint(1, 3)
 
 # initialize value of comp_choice_name 
 # variable corresponding to the choice value
 if comp_choice == 1:
 comp_choice_name = 'Rock'
 elif comp_choice == 2:
 comp_choice_name = 'paper'
 else:
 comp_choice_name = 'scissor'
 
 print("Computer choice is: " + comp_choice_name)
 print(game[comp_choice-1])

 
 print("\n" + choice_name + " V/s " + comp_choice_name + "\n")
 
 # condition for winning
 if((choice == 1 and comp_choice == 2) or
 (choice == 2 and comp_choice ==1 )):
 print("paper wins")
 result = "paper"
 
 elif((choice == 1 and comp_choice == 3) or
 (choice == 3 and comp_choice == 1)):
 print("Rock wins")
 result = "Rock"
 
 # Condition for draw
 elif(choice==comp_choice):
 print("Draw")
 result = 1
 
 else:
 print("scissor wins", end = "")
 result = "scissor"

 
 # Printing either user or computer wins
 if result == choice_name:
 print("== User wins ==")

 elif result == 1:
 print("== No one wins ==")
 
 else:
 print("== Computer wins ==")
 
 print("Do you want to play again? (Y/N)")
 ans = input()
 
 
 # if user input n or N then condition is True
 if ans == 'n' or ans == 'N':
 break
 
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing !!")
