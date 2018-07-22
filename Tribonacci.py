'''
description:
https://www.codewars.com/kata/556deca17c58da83c00002db
'''
def tribonacci(signature,n):
    r=signature
    if n==0:
        return []

    elif n<len(signature):
        return r[:n]
    else:
        for i in range(3,n):
            r.append(sum(r[i-3:i:1]))
    return r
