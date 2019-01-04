"""
our task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221

"""

def numdesc(num):
    n = list(str(num))
    num = []

    for i in n:
        print(i)
        num.append(i)

    num.sort()
    num.reverse()

    y = "".join(num)

    return int(y)

s = 1534924211

print(numdesc(s))