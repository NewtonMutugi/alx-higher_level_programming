#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 0:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(len(args) - 1))
        for i in range(1, len(args)):
            print("{:d}: {:s}".format(i, args[i]))
