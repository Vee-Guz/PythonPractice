#!/usr/bin/python3
import random


"""" Rock, Paper, Scissors """


print("Welcome to Rock, Paper, Scissors!")

options = ["rock", "paper", "scissors"]

my_choice = input("Choose your option: ").lower()   ## convert input string to all lowercase
bot_choice = random.choice(options)                 ## random module function choice will choose a string from variable options

print(f'The computer chose: {bot_choice}')

win = "You win!"
lose = "You lose!"

if my_choice == "rock" and bot_choice == "scissors":
    print(win)
elif my_choice == "paper" and bot_choice == "rock":
    print(win)
elif my_choice == "scissors" and bot_choice == "paper":
    print(win)
elif my_choice == bot_choice:
    print("Tie! Both you and computer chose: {}".format(my_choice))
else:
    print(lose)
'''elif my_choice == "scissors" and bot_choice == "rock":
    print(lose)
elif my_choice == "rock" and bot_choice == "paper":
    print(lose)
elif my_choice == "paper" and bot_choice == "scissors":
    print(lose)
else:
    print("Tie! Both you and computer chose {}".format(my_choice))'''

