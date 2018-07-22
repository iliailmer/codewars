"""
This kata is to practice simple string output.
Jamie is a programmer, and James' girlfriend.
She likes diamonds, and wants a diamond string from James.
Since James doesn't know how to make this happen, he needs your help.

###Task:

You need to return a string that displays a diamond shape on the screen using
asterisk ("*") characters.

The shape that will be returned from print method resembles a diamond,
where the number provided as input represents the number of *’s printed
on the middle line.
The line above and below will be centered and
will have 2 less *’s than the middle line.
This reduction by 2 *’s for each line continues until a
line with a single * is printed at the top and bottom of the figure.

Return null if input is even number or negative
(as it is not possible to print diamond with even number or negative number).

Please see provided test case(s) for examples.

Python Note

Since print is a reserved word in Python,
Python students must implement the diamond(n) method instead,
and return None for invalid input.
"""
def diamond(n):
    if n%2==0 or n<1:
        return None
    else:
        result = ""
        spaces =' '
        for i in range(0,n,1):
            if i<n//2:
                s=' '*(n//2-i)+'*'*(2*i+1)+'\n'
            elif i>n//2:
                s=' '*(i - n//2)+'*'*(2*(n-i-1)+1)+'\n'
            elif i==n//2:
                s='*'*n+'\n'
            result+=s
        return str(result)
    return None
