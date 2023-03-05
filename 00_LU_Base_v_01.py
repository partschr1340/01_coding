# Functions go here...
import random

# Checks that user answer yes or no to the question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes/no")


# Displays instructions, returns""
def instructions():
    print("********HOW TO PLAY********")
    print()
    print("=====The rules of the game go here=====")
    print()
    print("You put how much money you would like to play with.")
    print()
    print("The Programme will then run the money through a system and give you random animal")
    print("*These animals with either be a Horse [which makes you lose $1]")
    print("*A horse or zebra [which will make you lose $0.50]")
    print("*Or a Unicorn [Which wins $4]")
    return ""


# Checks that the user enters an integer between a low and high number.
def num_check(question, low, high):
    error = "Enter a number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low/ too high to give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Introduces the user to the game, adds decoration to each program
def statement_generator(statement, decoration):
    sides = decoration * 3

    greeting = " {} {} {} ".format(sides, statement, sides)
    top_bottom = prize_decoration * len(statement)

    top_bottom = "~" * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)

    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the game before?")

if played_before == "no":
    instructions()

print()

# Ask user much they want to play with...
how_much = num_check("How much would you like to play with?", 0, 10)

# set balance for testing purposes
balance = how_much

rounds_played = 0

play_again = input("press <enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print("========= Round #{}=========".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn(adds $4 to their balance.)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)

    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "-"
        balance -= 1

    else:
        # if the number is even, set the chosen item to horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "*"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "*"
        balance -= 0.5

    outcome = "You got a {}. Your balance is" \
              "${:.2f}.".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        # If balance is too low, exit the game and output a suitable message
        play_again = "xxx"
        print("Sorry, you have ran out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit.")
        print()

print()
print(f"Final balance: ${balance:.2f}")
