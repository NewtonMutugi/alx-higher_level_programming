#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    last = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            last += 1
    except IndexError:
        print()
        return last
    print()
    return last
