"""
Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34

But can you do it in 1 line of code and without any conditionals?

"""

def opposite(integer):
    return -1*integer

print(opposite(-34))
print(opposite(2))

"""
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
"""
