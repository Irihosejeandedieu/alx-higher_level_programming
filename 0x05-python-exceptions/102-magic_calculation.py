#!/usr/bin/python3

def magic_calculation(a, b):
    solution = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception("Too far")
            solution += (a ** b) / j
        except Exception:
            solution = b + a
            break
    return solution

