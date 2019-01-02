'''
Euler 001
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
t = 1
v = 0
uvalue = 10000
for t in range(1, uvalue):
    if (t % 3 == 0) or (t % 5 == 0):
        print(t)
        v = v + t

print("Total: ", v)
