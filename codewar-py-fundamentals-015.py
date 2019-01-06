"""
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("


Notes:

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is actually the expected result, not the input! (these languages are locked so that's not possible to correct it).

narrative of solution:
search the string for characters appearing more than once (loop? or regex?). Replace duplicate characters with '('. Replace all other characters with ')' - use a loop or use regex?

"""

def dupconvert(string):
    return string



print(dupconvert("din"), "| (((")
print(dupconvert("recede"), "| ()()()")
print(dupconvert("Success"), "| )())())")
print(dupconvert("(( @"), "| ))((")

"""

"""
