'''
description:
https://www.codewars.com/kata/556e0fccc392c527f20000c5
'''
def Xbonacci(signature,n):
    r=signature[:n]
    for i in range(len(signature),n):r.append(sum(r[-len(signature):]))
    return r
