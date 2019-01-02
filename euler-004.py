""" 
Euler 004 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
uvalue = 1000
lvalue = 100
pal = None
for t in range(100, uvalue):
    print ("Factor: ", t)
    
    for t2 in range(100, uvalue):
        inspect = t2 * t
#        print ("Check: ", t, " * ", t2, " = ", inspect)

        if str(inspect) == str(inspect)[::-1]:
            if pal is None or inspect > pal:
                pal = inspect
                print ("Inspect: ", inspect, " Pal: ", pal)

