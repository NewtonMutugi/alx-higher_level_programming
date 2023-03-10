#!/usr/bin/python3
def uppercase(str):
    for i in str:
	if ord(i) >= 97 and ord(i) <= 122:
	    i = chr(ord(i) - 32)
	print("{}".format(i), end="")
    print()


if __name__ == "__main__":
	    uppercase("holberton")
    uppercase("Holberton School 98 Battery street")
    uppercase("holberton")
    uppercase("Holberton School 98 Battery street")
