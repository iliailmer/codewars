"""
You have to code a function getAllPrimeFactors wich take an integer as parameter
and return an array containing its prime decomposition by ascending factors,
if a factors appears multiple time in the decomposition
it should appear as many time in the array.

exemple: getAllPrimeFactors(100) returns [2,2,5,5] in this order.

This decomposition may not be the most practical.

You should also write getUniquePrimeFactorsWithCount, a function which will
return an array containing two arrays: one with prime numbers appearing
in the decomposition and the other containing their respective power.

exemple: getUniquePrimeFactorsWithCount(100) returns [[2,5],[2,2]]

You should also write getUniquePrimeFactorsWithProducts an array containing
the prime factors to their respective powers.

exemple: getUniquePrimeFactorsWithProducts(100) returns [4,25]

Errors, if:

n is not a number
n not an integer
n is negative or 0
The three functions should respectively return [], [[],[]] and [].

Edge cases:

if n=0, the function should respectively return [], [[],[]] and [].
if n=1, the function should respectively return [1], [[1],[1]], [1].
if n=2, the function should respectively return [2], [[2],[1]], [2].
The result for n=2 is normal. The result for n=1 is arbitrary and
has been chosen to return a usefull result.
The result for n=0 is also arbitrary but can not be chosen
to be both usefull and intuitive.
([[0],[0]] would be meaningfull but wont work for general use of decomposition,
[[0],[1]] would work but is not intuitive.)
"""
def getAllPrimeFactors(n):
    if isinstance(n,str):
        return []
    i=2
    factors = []
    if n>0 and n!=1 and n!=2 and isinstance(n,int):
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n!=1:
            factors.append(n)
        return factors
    elif n<=0:
        return []
    elif n==1:
        return [1]
    elif n==2:
        return [2]
    else:
        return []


def getUniquePrimeFactorsWithCount(n):
    count=0
    l = getAllPrimeFactors(n)
    factors = [list(set(l))]
    C = []
    for each in set(l):
        for other in l:
            if each==other:
                count+=1
        C.append(count)
        count =0
    factors.append(C)
    return factors


def getUniquePrimeFactorsWithProducts(n):
    l = getUniquePrimeFactorsWithCount(n)
    factors = l[0]
    powers = l[1]
    products = []
    for i in range(len(factors)):
        products.append(factors[i]**powers[i])
    return products
