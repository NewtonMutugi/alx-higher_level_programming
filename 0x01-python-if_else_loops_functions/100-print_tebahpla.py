#!/usr/bin/python3
import sys

for i in range(122, 96, -1):
    letter = chr(i)
    condition = i % 2 != 0
    print(letter.upper() if condition else letter, end='')
sys.stdout.write('\n')
