from random import randint
from arts import logo
import os

run_time = 0

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
        run_time = 10
    elif level == 'hard':
        run_time = 5
    return run_time