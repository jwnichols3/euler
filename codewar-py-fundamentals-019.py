"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

narrative of solution:
Use the set function?


"""
def array_diff(lista=[], listb=[]):
    return (list(set(lista) - set(listb))) 
#    seta = set(lista)
#    setb = set(listb)

#    setdiff = lista - listb

#    return setdiff


print( array_diff ([1,2], [1]),   "| a was [1,2], b was [1], expected [2]" )
print( array_diff ([1,2,2], [1]), "| a was [1,2,2], b was [1], expected [2,2]]")
print( array_diff ([1,2,2], [2]), "| a was [1,2,2], b was [2], expected [1]")
print( array_diff ([1,2,2], []),  "| a was [1,2,2], b was [], expected [1,2,2]")
print( array_diff ([], [1,2]),    " | a was [], b was [1,2], expected []")


""" Sample Tests
Test.describe("Basic Tests")
Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")

"""
