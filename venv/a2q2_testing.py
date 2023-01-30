# Name: SM Shouvik Raj
# NSID: dew873
# Student Number: 11339451
# Course Number: CMPT-145-02
# Lab Section: 04

# asks user for file name
# example = input("Enter file name: ")


def distance(name):
    """
    Asks user for instruction file name and creates a list of list
    for each line of instructions
    :param name: name of file in .txt format, assuming file exists in same folder
     as program and has valid instructions i.e. 'R' and 'L'
    :post-condition: converts simple text in .txt file to a list of list
    :return: numerical displacement value
    """
    final = 0
    instructions = []
    f = open(name, 'r')
    r = f.read()
    answer = []
    lines = r.splitlines()
    for x in lines:
        instructions.append(x.split())
    for list1 in instructions:
        for value in list1:
            if value == 'R':
                final += 1
            else:
                final -= 1
        answer.append(abs(final))
        final = 0
    return answer


# distance(example)

# Test Cases:
def test_cases():
    test_case = 'distance("example1.txt")'
    input = 'example1.txt'
    expected = [0, 4, 4, 2, 9, 8, 3, 9, 7, 3, 1, 0, 8]
    output = distance(input)
    if output != expected:
        print("Test case {} failed on input {}, expected {}, "
              "got {}".format(test_case, input, expected, output))
    elif output == expected:
        test_case = 'distance("example2.txt")'
        input = 'example2.txt'
        expected = [2, 10, 0, 4, 1, 4, 1, 3, 1, 8, 1, 2, 2, 0, 6, 1, 1, 0, 4, 3, 0, 2, 2]
        output = distance(input)
        if output != expected:
            print("Test case {} failed on input {}, expected {}, "
                  "got {}".format(test_case, input, expected, output))
        elif output == expected:
            test_case = 'distance("example3.txt")'
            input = 'example3.txt'
            expected = [1, 3, 9, 1, 2, 2, 3, 4]
            output = distance(input)
            if output != expected:
                print("Test case {} failed on input {}, expected {}, "
                      "got {}".format(test_case, input, expected, output))


test_cases()
