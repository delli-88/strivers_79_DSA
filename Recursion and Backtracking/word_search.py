from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                vis = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
                if board[i][j]==word[0]:
                    vis[i][j] = 1
                    if self.existHelper(board, vis, word, i, j, 1):
                        return True
                
        return False
    
    def existHelper(self, board, vis, word, row, col, pos):
        row_len = len(board)
        col_len = len(board[0])
        if pos==len(word):
            return True
        vis[row][col]=1
        row_dirs = [-1,1,0,1]
        col_dirs = [0,0,-1,1]
        for i in range(4):
            curr_row = row+row_dirs[i]
            curr_col = col+col_dirs[i]
            if curr_row>=0 and curr_row<row_len and curr_col>=0 and curr_col<col_len and vis[curr_row][curr_col]==0 and board[curr_row][curr_col]==word[pos]:

                
                if self.existHelper(board, vis, word, curr_row, curr_col, pos+1):
                    return True
        vis[row][col]=0

        return False

print(Solution().exist( board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word = "ABCESEEEFS"))