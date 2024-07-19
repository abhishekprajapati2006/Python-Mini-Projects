# Project : Rock ,Paper ,Scissors Game
import random
rock = '''

    __________
---'    ______)
       (_______)
       (_______)
       (______)
---.___(_____)
'''

paper = '''
    __________
---'    ______)___
       (__________)_
       (____________)
       (_________)
---.___(_____)

'''

scissors = '''

    _________
---'    _____)___
       (_________)
       (__________)
       (_____)
---.___(____)

'''
invalid = '''
    __________
---'    ______)
       (_______)_____
       (_____________)
       (______)
---.___(_____)

'''

game_item = [ rock , paper, scissors]
user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n👉 "))
if user_number >=3 or user_number < 0  : print(f"You typed an invalid number, you loss!👎 : {invalid} fack U bro 🤘\n")
else : print(game_item[user_number])
computer_number = random.randint(0,2)
print(f"💻 Computer choose : {computer_number}")
print(game_item[computer_number])
if user_number == 0 and computer_number == 2 : print("You Win!🏆") 
elif computer_number == 0 and user_number == 2 : print("You loss!👎")
elif computer_number > user_number : print("You loss!👎") 
elif user_number > computer_number : print("You Win!🏆")
elif computer_number == user_number: print("It's a draw👐")