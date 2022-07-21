from random import randint
from arts import logo
import os


EASY_LEVEL = 10
HARD_LEVEL = 5

def clear():
    os.system('cls')

def check_answer(guess, answer):
    """Takes in guess and the answer and compares them"""
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You gote it! the answer is {answer}")

def set_difficulty():
    """Sets the difficulty level of the Game either to hard or easy"""
    level = input("Choose the level of difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a Number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attempts, to guess the number")
    

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)
        turns -= 1
game()