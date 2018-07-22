"""
In this kata, you should calculate type of triangle with three given sides a,
b and c (given in any order).

If all angles are less than 90°, this triangle is acute and
function should return 1.

If one angle is strictly 90°, this triangle is right and
function should return 2.

If one angle more than 90°, this triangle is obtuse and
function should return 3.

If three sides cannot form triangle, or one angle is 180°
(which turns triangle into segment) - function should return 0.

Input parameters are sides of given triangle.
All input values are non-negative floating point or integer numbers (or both).
"""

# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    """cosa=(a**2-(b**2+c**2))/2*b*c
    cosb=(b**2-(a**2+c**2))/2*a*c
    cosc=(c**2-(a**2+b**2))/2*b*a
"""
    l =list((a,b,c))
    l.sort()
    if (a>=b+c)or (b>=c+a) or (c>=a+b):
        return 0
    if (l[2]**2<l[0]**2+l[1]**2):
        return 1
    if (l[2]**2==l[0]**2+l[1]**2):
        return 2
    if (l[2]**2>l[0]**2+l[1]**2):
        return 3
