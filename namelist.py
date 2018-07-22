'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by
commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain
A-Z, a-z, '-' and '.'.
'''

def namelist(names):
    a=''
    #for each in names:
        #a=a+' '.join(each[key] for key in each)
    a=', '.join(each[key] for each in names for key in each)[::-1].replace(' ,',' & ',1)
    a=a[::-1]
    return a
