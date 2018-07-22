"""
Write a function done_or_not/DoneOrNot
passing a board (list[list_lines]) as parameter.
If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column,
and region contains the numbers one through nine only once.

Rows:
There are 9 rows in a traditional Sudoku puzzle.
Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
There may not be any duplicate numbers in any row.

In other words, there can not be any rows that are identical.

Columns:
There are 9 columns in a traditional Sudoku puzzle.
Like the Sudoku rule for rows, every column must also contain the numbers
1, 2, 3, 4, 5, 6, 7, 8, and 9.
Again, there may not be any duplicate numbers in any column.

Each column will be unique as a result.

Columns:
A region is a 3x3 box like the one shown to the left.
There are 9 regions in a traditional Sudoku puzzle.
Like the Sudoku requirements for rows and columns,
every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
Duplicate numbers are not permitted in any region.

Each region will differ from the other regions.
"""
def check_squares(board):
    s=''
    sm=0
    got_box=True
    for k in range(3):
        for p in range(3):
            for i in range(3*k,3*k+3):
                for j in range(3*p,3*p+3):
                    sm+=board[i][j]
            if sm==45:
                got_box*=True
                sm=0
            else:
                got_box*=False
    return bool(got_box)

def done_or_not(board): #board[i][j]
    checking_set = list(range(1,10))
    cols = []
    got_rows=True
    got_cols=True
    got_squares=check_squares(board)
    for each in board:
        if sum(each)==sum(checking_set):
            got_rows=True
        else:
            got_rows=False
    for col in range(9):
        for row in range(9):
            cols.append(board[row][col])
        if sum(cols)==sum(checking_set):
            got_cols=True
        else:
            got_cols=False
        cols = []
    if got_rows and got_cols and got_squares:
        return 'Finished!'
    else:
        return 'Try again!'
