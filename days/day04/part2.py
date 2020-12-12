import sys
import copy
import collections

def get_sequences(s):
    return [s.count(c) for c in set(s)]

def check_adjacent(s):
    seqs = get_sequences(s)
    seqs = map(lambda x: x ==2, seqs)
    return any(seqs)

sum = 0
for xx in range(146810, 612564):
    s = "%d" % xx
    valid = True
    for c in range(1, len(s)):
        if int(s[c-1]) > int(s[c]):
            valid = False
            break

    valid = valid & check_adjacent(s)
    if valid:
        sum += 1

print(sum)

        


