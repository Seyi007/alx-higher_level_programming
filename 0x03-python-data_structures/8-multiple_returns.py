#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_sen = ()
    length = len(sentence)
    first = sentence[0]

    if length == 0:
        tuple_sen = 0, None
    else:
        tuple_sen = length, first
    return tuple_sen
