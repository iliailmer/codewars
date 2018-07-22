'''description:
https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
'''

def validate(n):
    l=map(int,list(str(n)))
    if len(l)%2==0:
        i=0
        while (i+2)<=len(l):
            l[i]=l[i]*2
            if l[i]>9:
                l[i]-=9
            i+=2
    else:
        j=1
        while (j+2)<=len(l):
            l[j]=l[j]*2
            if l[j]>9:
                l[j]-=9
            j+=2

    if sum(l)%10==0:
        return True
    else:
        return False
