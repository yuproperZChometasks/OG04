

import random

def main():
    user_wins = 0
    computer_wins = 0
    winning_score = 3

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Человек"
    else:
        return "Компьютер"

