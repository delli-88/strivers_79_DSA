from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solveSudokuHelper(board)
        return board
    
    def solveSudokuHelper(self, board):
        row, col = self.find_empty_cell(board)
        if row==None and col==None:
            return True
        
        for num in range(1,10):
            if self.can_we_place(num, row, col, board):
                board[row][col] = str(num)
                
                if self.solveSudokuHelper(board):
                    return True
                else:
                    board[row][col]="."
        return False
    
    def find_empty_cell(self, board):
        row, col = None, None

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    return (i,j)
        return (row, col)
    
    def can_we_place(self, num, row, col, board):

        num_str = str(num)
        #check row
        for i in range(9):
            if board[i][col]==num_str:
                return False

        #check col
        for i in range(9):
            if board[row][i]==num_str:
                return False

        #check box
        extra_rows = row%3
        row_start = row - extra_rows

        extra_cols = col%3
        col_start = col - extra_cols

        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                if board[i][j]==num_str:
                    return False
        return True
                

    

# print(Solution().solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(Solution().solveSudoku(board = [[".",".",".",".","8",".",".",".","9"],[".","6",".","9",".",".","1","8","."],[".",".","4",".","3",".",".",".","."],["1",".",".","5",".","4",".",".","6"],[".",".",".","3",".","7","5","4","."],[".",".",".",".",".",".",".",".","."],["5",".","7",".",".",".",".","1","."],["8","4",".",".",".","3",".",".","."],[".",".","9",".",".",".","7",".","2"]]))


'''
Problem : https://leetcode.com/problems/sudoku-solver/description/
TC : O(9^(n^2))
SC : O(1)
Approach :
1. Create a `solve` function that takes the Sudoku board as input.
2. Loop through each cell in the board:
   - If the cell is empty (contains "."), loop from 1 to 9:
     - Check if placing a number (as a string) in that cell is valid using the `is_valid` function.
     - If it's valid, set the cell to that number and recursively call `solve` on the updated board.
     - If `solve` returns `True`, the Sudoku is solved, so return `True`.
     - If not, backtrack by setting the cell back to "." and continue trying the next number.
   - If the cell is not empty, move on to the next cell.
3. If all cells are filled, return `True` (Sudoku is solved).
4. If no valid number can be placed in the current cell, return `False` to trigger backtracking.
5. The `is_valid` function checks if a number can be placed in a cell without violating Sudoku rules (no repeated numbers in the same row, column, or 3x3 box).

''' 