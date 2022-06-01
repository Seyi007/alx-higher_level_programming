#!/usr/bin/python3
for alpha in range(ord('a'), ord('z')):
    if alpha is not (ord('q') and ord('e')):
        print("{:c}".format(alpha), end="")
