# Name: SM Shouvik Raj
# NSID: dew873
# Student Number: 11339451
# Course Number: CMPT-145-02
# Lab Section: 04

# asks user for file name
example = input("Enter file name: ")
def distance(name):
    """
    Asks user for instruction file name and creates a list of list
    for each line of instructions
    :param name: name of file in .txt format, assuming file exists in same folder
     as program and has valid instructions i.e. 'R' and 'L'
    :post-condition: converts simple text in .txt file to a list of list
    :return: numerical displacement value
    """
    instructions = []
    f = open(name, 'r')
    r = f.read()
    lines = r.splitlines()
    for x in lines:
        instructions.append(x.split())
    return instructions

distance(example)

