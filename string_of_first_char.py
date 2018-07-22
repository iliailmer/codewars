'''
In this exercise, a string is passed to a method and a new
string has to be returned with the first character of each word in the string.

For example:

"This Is A Test" ==> "TIAT"
'''

def make_string(s):
    x=s.split(" ");
    res=""
    for each in x:
        res=res+each[0]
    return res
