#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    chars = len(roman_string) - 1
    for i, c in enumerate(roman_string):
        if hi < cars and roman_dict[c] < roman_dict[roman_string[i + 1]]:
            total -= roman_dict[c]
        else:
            total += roman_dict[c]
    return total
