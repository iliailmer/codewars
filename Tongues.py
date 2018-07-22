'''
description
https://www.codewars.com/kata/52763db7cffbc6fe8c0007f8
'''

def tongues(code):
    import string
    rot13 = string.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","EPLRAGFSOXVCWTIBZDHNYKMJUQeplragfsoxvcwtibzdhnykmjuq")
    return string.translate(code,rot13)
