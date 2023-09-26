from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for _ in range(n):
            board.append(["."]*n)
        return self.helper(0,board,[],n)
    def helper(self,r,board,sol_arr,n):
        if n==0:
            new1 = []
            for _ in range(len(board)):
                str1 = "".join(board[_])
                new1.append(str1)
            sol_arr.append(new1)
            return sol_arr
        
        for col in range(len(board[0])):
            safe = self.is_safe(r,col,board)
            if safe:
                board[r][col] = 'Q'
                self.helper(r+1,board,sol_arr,n-1)
                board[r][col] = '.'
        
        return sol_arr

    def is_safe(self,r,c,arr):
        #top
        top = True
        x = r-1
        y = c
        while x>=0:
            if arr[x][y]=='Q':
                top = False
                break
            x-=1
        #leftdiag
        ldiag = True
        x = r-1
        y = c-1
        while x>=0 and y>=0:
            if arr[x][y]=='Q':
                ldiag = False
                break
            x-=1
            y-=1
        #rightdiag
        rdiag = True
        x = r-1
        y = c+1
        while x>=0 and y<len(arr[0]):
            if arr[x][y]=='Q':
                rdiag = False
                break
            x-=1
            y+=1
        if top and ldiag and rdiag:
            return True
        else:
            return False

'''
Problem : https://leetcode.com/problems/n-queens/description/
TC : O(n! * n)
SC : O(n^2)
Approach : 

1. Define a recursive helper function `helper` that takes four parameters:
   - `r`: the current row being considered.
   - `board`: the current state of the chessboard, represented as a list of lists.
   - `sol_arr`: the list to store valid solutions.
   - `n`: the number of queens to place (decreases with each placement).
2. In the `helper` function:
   - If `n` reaches 0, it means all queens have been successfully placed on the board. In this case, convert the `board` representation to a list of strings, where 'Q' represents a queen and '.' represents an empty cell. Append this solution to the `sol_arr` list.
   - Iterate through each column in the current row `r` and check if it's a safe position to place a queen using the `is_safe` function.
   - If the position is safe, mark it as 'Q' on the board, and recursively call `helper` for the next row (`r+1`) with the updated board and `n-1`.
   - After the recursive call, backtrack by resetting the cell to '.' to explore other possibilities.
3. Define the `is_safe` function to check if a queen can be safely placed at a given position `(r, c)` on the board. This function checks three conditions:
   - No queens in the same column (top).
   - No queens in the left diagonal.
   - No queens in the right diagonal.
   If all three conditions are met, the position is considered safe.
4. Initialize an empty chessboard `board` with dimensions `n x n`, initially filled with '.' characters.
5. Start the recursion by calling `helper(0, board, [], n)` to find all solutions with the first row as the starting point.
6. Return the `sol_arr` list containing all valid solutions.

'''

'''
//Another solution

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        return self.solveNQueensHelper(n, board, 0, 0, n, [])
    
    def solveNQueensHelper(self, n, board, row, col, queens, sol):
        if row==0 and col==n:
            return sol
        
        if row==n:
            if queens==0:
                new_board = []
                for i in range(n):
                    new_board.append("".join(board[i][:]))
                sol.append(new_board[:])
            return sol
        
        if col==n:
            # self.solveNQueensHelper(n, board, row+1, 0, queens, sol)
            return sol
        else:

            if self.isQueenSafe(n, board, row, col):
                board[row][col] = "Q"
                self.solveNQueensHelper(n, board, row+1, 0, queens-1, sol)
                board[row][col] = "."
            
            self.solveNQueensHelper(n, board, row, col+1, queens, sol)
        
        return sol
        
    
    def isQueenSafe(self, n, board, row, col):
        if board[row][col]=="Q":
            return False
        
        # row
        for i in range(n):
            if board[i][col] == "Q":
                return False
        
        #col
        for i in range(n):
            if board[row][i] == "Q":
                return False
        
        #top-left
        temp_row = row-1
        temp_col = col-1

        while temp_row>=0 and temp_col>=0:
            if board[temp_row][temp_col]=="Q":
                return False
            temp_row-=1
            temp_col-=1
        
        #top-right
        temp_row = row-1
        temp_col = col+1

        while temp_row>=0 and temp_col<n:
            if board[temp_row][temp_col]=="Q":
                return False
            temp_row-=1
            temp_col+=1
    
        #bottom-left
        temp_row = row+1
        temp_col = col-1

        while temp_row<n and temp_col>=0:
            if board[temp_row][temp_col]=="Q":
                return False
            temp_row+=1
            temp_col-=1

        #bottom-right
        temp_row = row+1
        temp_col = col+1

        while temp_row<n and temp_col<n:
            if board[temp_row][temp_col]=="Q":
                return False
            temp_row+=1
            temp_col+=1

        return True
    
print(Solution().solveNQueens(4))
'''