#!/usr/bin/python3
n range(ord('a'), ord('z') + 1):
    if n not in (ord('e'), ord('q')):
        print("{}".format(chr(n)), end='')
