# This is a simple Rock, Paper, Scissors game. Scissors beats paper,
# paper beats rock, rock beats scissors. Enjoy!

# Author: The Tuesdays section of Newton GWC 2016-2017.

# TODO(future): implement a 2-player mode

# TODO(future): Make buttons to harvest input

# TODO: Read input, assign to RPS

import random

actions = ["rock", "paper", "scissors"]

# TODO: Find out if python has a goto function
# SNARKY TODO: Don't use it. I hate goto

# TODO: Add pictures
def game():
    user_input = raw_input(
        "Choose rock, paper, or scissors\n---> ")

    # TODO: check that the user typed only one
    # of these choices

    # TODO: Make a variable for the conmputer's
    # choice

    computer_input = random.choice(actions)

    # TODO(stella): print what the computer chose
    print computer_input

    # TODO: Make a conditional test of what the user has,
    # what the computer has, who wins
    # do this for all circumstances

    # TODO: Check if python does switch statements
    # TODO(sara): Re-implment this using an array!
    # The case of a ties
    # TODO(ella): Re-implement this with an enumeration
    # of the rules.

    # TODO(antonia): put the game play in a method
    # to allow us to play multiple times.
    if user_input == computer_input:
        print "It's a tie"

    # All the computer rock combinations
    elif computer_input == "rock" and user_input == "paper":
        print "you win"
    elif computer_input == "rock" and user_input == "scissors":
        print "you lose"

    # All the computer paper combinations
    elif computer_input == "paper" and user_input == "scissors":
        print "you win"
    elif computer_input == "paper" and user_input == "rock":
        print "you lose"

    # All the computer scissors combinations

    elif computer_input == "scissors" and user_input == "paper":
        print "you lose"
    elif computer_input == "scissors" and user_input == "rock":
        print "you lose"
    else:
        print "please type in rock, paper, or scissors exactly"
    # TODO: have an error clause for complaining if the
    # input is not R P or S

    print "try again"

while True:
    game()



