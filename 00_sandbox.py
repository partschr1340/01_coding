def statement_generator(statement, decoration):
    sides = decoration * 3

    greeting = " {} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    top_bottom = "=" * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)

    return ""


# Main routine goes here
statement_generator("WELCOME TO THE LUCKY UNICORN GAME", "*")
print()
statement_generator("Congratulations, you got a UNICORN", "!")
