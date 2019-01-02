""" 
Euler 003 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
"""
uvalue = 600851475143 # upper value
i = 2       # starting point
print ("Value: ", uvalue)
while i * i < uvalue:
    print ("Increment: ", i, " is: ", (i * i))
    while uvalue % i == 0:
        print ("evaluating: ", uvalue, " divided by: ", i)
        uvalue = uvalue / i
    i = i + 1
    print ("Factored uvalue:", uvalue)

print ("Final answer: ", uvalue)

    