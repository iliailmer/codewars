'''
Complete the squareSum/square_sum/SquareSum method so
that it squares each number passed into it and then sums the results together.

For example:

square_sum([1, 2, 2]) # should return 9
'''
def square_sum(numbers):
    square_sum=sum( x**2  for x in numbers)
    return square_sum
