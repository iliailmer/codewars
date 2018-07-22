"""
Write a function that calculates the least common multiple of its arguments;
each argument is assumed to be a non-negative integer.
In the case that there are no arguments (or the provided array
in compiled languages is empty), return 1.
"""

def gcd(a,b):
    """Euclid's Algorithm"""
    while b>0:
        flag = b
        b = a%b
        a = flag
    return a

def lcm_two_args(a,b):
    if a==0 or b==0:
        return 0
    else:
        return a*b//(gcd(a,b))

def lcm(*args):
    if len(args)==1:
        return args[0]
    if len(args)==2:
        return lcm_two_args(*args)
    else:
        return reduce(lcm, args)
