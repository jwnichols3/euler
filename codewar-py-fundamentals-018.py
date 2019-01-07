"""
Write function avg which calculates average of numbers in given list.

Python:

Due to rounding issues please do not use statistics.mean or such.
If the array is empty, return 0.

narrative of solution:
Does numpy have a function for this?

"""

def find_average(array=0):
    if (type(array) != list) or (len(array) == 0):
        return 0

    return sum(array) / len(array)


print(find_average(), "| 0")
print(find_average([]), "| 0")
print(find_average([1, 2, 3]), "| 2")
print(find_average([10, 11, 12, 13, 14, 15]), "| 12.5")
print(find_average([6, 2, 1, 8, 10]), "| 5.4")
print(find_average([-6, -20, -1, -10, -12]), " | -9.8")


""" Sample Tests
array = [ 1, 2, 3 ]
Test.assert_equals(find_average(array), 2)

"""
