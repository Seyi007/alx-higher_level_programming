#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = len(argv)
    if num == 1:
        print("{} argument.".format(num - 1))
    else:
        print("{} argument:".format(num - 1))

    for args in range(1, num):
        print("{}: {}".format(args, argv[args]))
