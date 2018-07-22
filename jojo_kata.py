'''
description:
https://www.codewars.com/kata/55327e12f5363713200000e4
'''

regex="" #your regex here or...

def is_jojo(name):
    s1=name.split(' ')
    s=[s1[0],s1[len(s1)-1]]
    if (s[0].startswith('Jo') and s[1].startswith('Jo') or s[0].startswith('Gio') and s[1].startswith('Gio') or s[0].startswith('Jo') and s[1].endswith('jo')):
        return True
    else:
        return False
