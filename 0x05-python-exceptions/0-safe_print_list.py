#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    numbers = 0
    try:
        for num in range(x):
            print ("{}".format(my_list=[num]), end='')
            num += 1
    except IndexError:
        pass
    print()
    return numbers
