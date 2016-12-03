import random

choices = ["rock", "paper", "scissors"]
while True:
    user_choice = raw_input("rock, paper, or scissors? ")
    if (user_choice not in choices):
        print "Sorry, you must type \"rock\", \"paper\", or \"scissors\" (all lower-case)."
        print "You typed: \"" + user_choice + "\"."
        exit()

    computer_choice = random.choice(choices)

    print "\n"
    print "I chose " + computer_choice + "."
    print "You chose " + user_choice + "."
    print "\n"

    if (user_choice == "rock" and computer_choice == "paper"):
        print "I win!"

    elif (user_choice == "rock" and computer_choice == "scissors"):
        print "You win!"

    elif (user_choice == "paper" and computer_choice == "scissors"):
        print "I win!"

    elif (user_choice == "paper" and computer_choice == "rock"):
        print "You win!"

    elif (user_choice == "scissors" and computer_choice == "rock"):
        print "I win!"

    elif (user_choice == "scissors" and computer_choice == "paper"):
        print "You win!"

    else:
        print "It's a tie!"

    print "\nLet's play again"



