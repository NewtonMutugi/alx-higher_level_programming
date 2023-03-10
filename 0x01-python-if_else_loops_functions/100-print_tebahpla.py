#!/usr/bin/python3
for i in range(122, 96, -1):
    letter = chr(i)
    condition = i % 2 != 0
    print("{}".format(letter.upper() if condition else letter), end='')
print()
