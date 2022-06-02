#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num = len(sys.argv)
    if num == 1:
        print("{} argument.".format(num - 1))
    if num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} argument:".format(num - 1))

    for args in range(1, num):
        print("{}: {}".format(args, sys.argv[args]))
