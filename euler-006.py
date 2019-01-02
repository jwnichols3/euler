""" 
Euler 006
2The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
toprange = 100 # top-end of the number set (e.g. 1-10)
t = 0
t2 = 0

for i in range(1, toprange+1):
    t = t + (i**2)
    t2 = t2 + i

t3 = t2**2
t4 = t3 - t
print ("Difference between square of first", toprange, "numbers (", t, ") and the square of the sum (", t2, "/", t3, ") is", t4)
