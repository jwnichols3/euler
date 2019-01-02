""" 
Euler 007
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
-------------------------------------------------------
This is an effective but inefficient way to check this. 
"""
# Function returns True if prime, False if not
def primecheck(x):
    for i in range(2, int(x/2)):
        if x % i  == 0:
            return False
    else:
        return True

# Main
toprange = 10001 # how many to find
t = 2 # starting number
count = 0 # how many primes found
primelist = [] # array of primes

while count <= toprange:
    x = primecheck(t)
#    print("Checking", t, "for prime:", x)
    if x:
        primelist.append(t)
        count = count + 1
        # print("Primes found:", count, t)
    t = t + 1

print(toprange, "prime:", primelist[-1])

