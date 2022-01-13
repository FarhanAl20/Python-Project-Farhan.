# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:10:17 2022

@author: WIN7
"""

#Farhan Al Ikhsan Coding Nih :D
print("selamat datang di program game saya")
print("yg berjudul Rock,Paper,Scissors")
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 3

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 3

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 3

    else:
        print("You lost!")
        computer_wins += 3

print("You win", user_wins, "times.")
print("The computer win", computer_wins, "times.")
print("Goodbye and Thanks you")
print("lebih kurang saya mohon maaf dalam pembuatan progran ini")