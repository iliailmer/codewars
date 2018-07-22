'''
description:
https://www.codewars.com/kata/55d38b959f9c33f3fb00007d
'''
def adjust(coin, price):
    k=price
    while not(k%coin==0 and price<=k):
        k+=1
    return k
