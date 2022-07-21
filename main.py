from random import randint
from arts import logo
import os


EASY_LEVEL = 10
HARD_LEVEL = 5

def clear():
    os.system('cls')

def check_answer(guess, answer, turns):
    """Takes in guess and the answer, compares them and returns the number of turns remaining """
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
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
    """Main functionality of game"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a Number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts, to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of lives, You lose!")
            return
game()
while input("\nDo you wish to play again, yes or no?: ") == 'yes':
    clear()
    game()