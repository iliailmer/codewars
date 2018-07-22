'''
Oh no, Timmy's filter doesn't seem to be working?
Your task is to fix the FilterNumber function to
remove all the numbers from the string.
'''

def filter_numbers(string):
    return "".join( x for x in string if not(x>="0"and x<="9"))
