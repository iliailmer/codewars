'''
description:
https://www.codewars.com/kata/52761ee4cffbc69732000738
'''
def goodVsEvil(good, evil):
    g_side=[1,2,3,3,4,10]
    e_side=[1,2,2,2,3,5,10]
    g=good.split(" ")
    e=evil.split(" ")
    gprod=0
    eprod=0
    for i in range(len(g)):
        g[i]=int(g[i])
        gprod+=g[i]*g_side[i]

    for j in range(len(e)):
        e[j]=int(e[j])
        eprod+=e[j]*e_side[j]

    if gprod>eprod:
        return 'Battle Result: Good triumphs over Evil'
    elif gprod<eprod:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
