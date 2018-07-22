'''
Imagine there's a big cube consisting of n^3 small cubes.
Calculate, how many small cubes are not visible from outside.

For example, if we have a cube which has 4 cubes in a row,
then the function should return 8, because there are 8 cubes
inside our cube (2 cubes in each dimension)

'''
def not_visible_cubes(n):
    if n<3:
        return 0
    else:
        return n**3-2*n**2-(n-2)*n*2-(n**2-2*n-(n-2)*2)*2
