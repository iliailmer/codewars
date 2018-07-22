'''
The prime numbers are not regularly spaced.
For example from 2 to 3 the step is 1.
From 3 to 5 the step is 2. From 7 to 11 it is 4.
Between 2 and 50 we have the following pairs of 2-steps primes:

3, 5 - 5, 7, - 11, 13, - 17, 19, - 29, 31, - 41, 43

We will write a function step with parameters:

g (integer >= 2) which indicates the step we are looking for,
m (integer >= 2) which gives the start of the search (m inclusive),
n (integer >= m) which gives the end of the search (n inclusive)
In the example above step(2, 2, 50) will return [3, 5]
which is the first pair between 2 and 50 with a 2-steps.

So this function should return the first pair of the
two prime numbers spaced with a step of g between the limits m, n
if these g-steps prime numbers exist otherwise nil or null or None or Nothing
or [] or "0, 0" or {0, 0} (depending on the language).
'''
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i != 0:
            continue
        else:
            return False
    return True

def step(st, start, end):
    for n in range(start, end+1):
        if (is_prime(n)):
            if n+st<end and is_prime(n+st):
                return [n,n+st]
        else:
            continue
    return None
