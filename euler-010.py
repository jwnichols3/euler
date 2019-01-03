""" 
Euler 010
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
# Function returns True if prime, False if not
def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

psum = 0
ulimit = 100000

for y in range(1, ulimit):
    if is_prime_number(y):
        psum = psum + y
#        print(y)

print("Sum:", psum)