"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.


narrative of solution:
Define a vowel set. (research how to use sets)
use the set to search the string to count the number of instances.
return the count.

"""

def getCount(inputStr):
    num_vowels = 0
    inputStr.lower()
    vowels = set('aeiou')

    for i in vowels:
        num_vowels = num_vowels + inputStr.count(i)

    return num_vowels



print(getCount("abracadabra"), "| 5")


"""
test.assert_equals(getCount("abracadabra"), 5)
"""
