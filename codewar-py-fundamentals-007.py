"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""

def oddint(num):
    n = list(str(num))
    retval = 0

    for i in range(1,9):
        if n.count(str(i)) % 2 != 0:
            retval = i
            break

    return retval

s = 22111556677
print(oddint(s))