'''
description:
https://www.codewars.com/kata/541c8630095125aba6000c00
'''

def digital_root(n):
    l=list(str(n))
    s=1000
    while s>10:
        s=0
        for i in range(len(l)):
            s+=int(l[i])
        l=list(str(s))
    return s
