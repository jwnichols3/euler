""" 
Euler 005
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

This is not an efficient method, but it is effective

toprange = 20 # top-end of the number set (e.g. 1-10)
t = 1
t2 = 0
found = False
results = []

while not found:
    val1 = t * toprange
    print(t, " : ", val1)
    results.clear()

    # run through the range and see if val1 is divisible by all numbers in the range
    for t2 in range(1, toprange):

#        print ("checking if mod", t2, "/", val1, " is zero: ", val1 % t2)

        results.append(val1 % t2)
        if (val1 % t2) > 0:
            break
        
        # if we've made it here, then all the mod results are zero
        if t2 == (toprange - 1):
            print("Factor reached: ", val1)
            print ("Results: ", results)
            found = True
            break

    t = t + 1
"""

# Highly efficient and effective version.

def gcd(x,y): return y and gcd(y, x % y) or x
def lcm(x,y): return x * y / gcd(x,y)

n = 1
for i in range(1, 21):
     n = lcm(n, i)
print(n)