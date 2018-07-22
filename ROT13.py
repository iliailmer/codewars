'''
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled.
Maybe you can decipher it? According to Wikipedia,
ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently
used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters.
Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
'''
def rot13(message):
    res=''
    for x in message:
        if x.isspace() or x.isdigit():
            res+=x
        elif x.isalpha() and (x>='A' and x<='M'or x>='a' and x<='m'):
            res+=(chr(ord(x)+13))
        elif x.isalpha() and (x>='N' and x<= 'Z' or x>='n' and x<='z'):
            res+=(chr(ord(x)-13))
        else:
            res+=x

    return res
