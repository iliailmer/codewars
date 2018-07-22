'''
In the following 6 digit number:

283910
91 is the greatest sequence of 2 consecutive digits.

In the following 10 digit number:

1234567890
67890 is the greatest sequence of 5 consecutive digits.

Complete the solution so that it returns the greatest sequence of f
ive consecutive digits found within the number given.
The number will be passed in as a string of only digits.
It should return a five digit integer.
The number passed may be as large as 1000 digits.
'''
import re
def solution(digits):
    m=-1
    p = re.search(r"([0-9][0-9][0-9][0-9][0-9])",digits)
    while(len(digits)>=5):
        if int(p.group(0))>=m:
            m=int(p.group(0))
            digits = digits[1:]
            p = re.search(r"([0-9][0-9][0-9][0-9][0-9])",digits)
        else:
            digits = digits[1:]
            p = re.search(r"([0-9][0-9][0-9][0-9][0-9])",digits)
    return m
