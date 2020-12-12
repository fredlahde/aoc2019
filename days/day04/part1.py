import sys
import copy

def check_adjacent(s):
    for c in range(1, len(s)):
        if s[c-1] == s[c]:
            return True
    return False

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

        


