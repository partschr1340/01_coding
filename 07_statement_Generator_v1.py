
def statement_generator(statement, decoration) :

    sides = decoration * 3
    
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)