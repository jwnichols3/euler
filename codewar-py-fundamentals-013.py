"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.

"""

def likes(list_of_names):
    l = len(list_of_names)

    if l == 0:
        return "no one likes this"
    if l == 1:
        return list_of_names[0] + " likes this"
    if l == 2:
        return list_of_names[0] + " and " + list_of_names[1] + " like this"
    if l == 3:
        return list_of_names[0] + ", " + list_of_names[1] + " and " + list_of_names[2] + " like this"

    return list_of_names[0] + ", " + list_of_names[1] + " and " + str(len(list_of_names)-2) + " others like this"


print(likes([]), "| no one likes this")
print(likes(["Peter"]), "| Peter likes this")
print(likes(["Jacob","Alex"]), "| Jacob and Alex like this")
print(likes(["Max","John","Mark"]), "| Max, John and Mark like this")
print(likes(["Alex","Jacob","Mark","Max"]), "| Alex, Jacob and 2 others like this")
print(likes(["Alex","Jacob","Mark","Max","Name1","Name2"]), "| Alex, Jacob and 4 others like this")

"""
Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
"""
