class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Prepare a hash set for each condition
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        # Iterate through each cell
        for i in range(9):
            for j in range(9):
                # Ignore the cell if it is '.'
                n = board[i][j]
                if n == '.':
                    continue
                # If already in this row, column, or square, return False
                if n in rows[i] or n in cols[j] or n in squares[i//3][j//3]:
                    return False
                # Otherwise, add to this row, column, and square
                rows[i].add(n)
                cols[j].add(n)
                squares[i//3][j//3].add(n)
        # If we get all the way through without a conflict, return True
        return True