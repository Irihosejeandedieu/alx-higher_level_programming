#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    numbers = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            numbers = numbers + 1
        except (TypeError, ValueError):
            pass
    print("")
    return numbers
