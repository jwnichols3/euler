"""
write this function accum.

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

"""

def accum(x):
    retval = ""
    repeat = 1
    count = len(x)

    for i in x:
        newword = i*repeat
        newword = str.capitalize(newword)
        if not count == repeat:
            newword = newword + "-"
        retval = retval + newword
        repeat = repeat + 1

    return retval
"""
        while rep2 <= rep1:
            retval.append(i)
            rep2 = rep2 + 1
        rep1 = rep1 + 1
        retval.append("-")
"""

s = 'abcd'

print(accum(s))