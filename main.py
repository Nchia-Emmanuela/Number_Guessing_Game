from random import randint
from arts import logo
import os

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