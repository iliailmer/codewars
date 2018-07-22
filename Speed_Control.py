'''
In John's car the GPS records every s seconds the distance travelled from
an origin (distances are measured in an arbitrary but consistent unit).
For example, below is part of a record with s = 15:

x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
The sections are:

0.0-0.19, 0.19-0.5, 0.5-0.75, 0.75-1.0, 1.0-1.25, 1.25-1.50, 1.5-1.75,
1.75-2.0, 2.0-2.25
We can calculate John's average hourly speed on every section and we get:

[45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]
Given s and x the task is to return as an integer the *floor* of
the maximum average speed per hour obtained on the sections of x.
If x length is less than or equal to 1 return 0 since the car didn't move.

#Example: with the above data your function gps(x, s)should return 74
'''
from math import floor

def gps(s, x):
    avg=list(range(0,len(x)))
    for i in range(1,len(x)):
        avg[i]=(abs(x[i]-x[i-1])/(s/3600))
    if len(avg)==0:
        return 0
    else:
        return floor(max(avg))
