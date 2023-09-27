from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        vis = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.existHelper(board, vis, word, i, j, 1):
                        return True
        return False
    
    def existHelper(self, board, vis, word, row, col, pos):
        row_len = len(board)
        col_len = len(board[0])
        if pos==len(word):
            return True
        vis[row][col]=1
        row_dirs = [-1,1,0,0]
        col_dirs = [0,0,-1,1]
        for i in range(4):
            curr_row = row+row_dirs[i]
            curr_col = col+col_dirs[i]
            if curr_row>=0 and curr_row<row_len and curr_col>=0 and curr_col<col_len and vis[curr_row][curr_col]==0 and board[curr_row][curr_col]==word[pos]:
                if self.existHelper(board, vis, word, curr_row, curr_col, pos+1):
                    return True
        vis[row][col]=0
        return False

print(Solution().exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(Solution().exist( board = [["A","a","a"],["a","A","A"],["A","a","a"],["A","a","a"]], word = "aaaaAaAa"))


'''
Problem : https://leetcode.com/problems/word-search/
TC : O(N * M * 4^L)
SC : O(O(L + N * M))
Approach :
1. Initialize a function `dfs` that performs depth-first search (DFS) to explore the board and check if it's possible to find the given word starting from a specific cell `(row, col)`
2. In the `dfs` function:
   - Check if the current position `pos` is equal to the length of the word. If it is, return `True` because the entire word has been found.
   - Check if the current `(row, col)` position is out of bounds or if the character at that position does not match the character in the word at position `pos`. If either condition is met, return `False`.
   - Store the original character at `(row, col)` in a variable `original_char` and mark the cell as visited by setting it to `"#"`.
   - Recursively explore in all four directions (up, down, left, and right) by calling `dfs` with the updated positions `(row +/- 1, col)` and `(row, col +/- 1)` while incrementing `pos` by 1.
   - If any of the recursive calls return `True`, it means a valid path to complete the word was found, so return `True`.
   - If none of the paths lead to a valid solution, backtrack by restoring the original character at `(row, col)` and return `False`.
3. Iterate through all cells in the board:
   - If a cell contains the first character of the word and a successful DFS search from that cell returns `True`, return `True` as the word can be found.
4. If no path in the board leads to a valid word, return `False`, indicating that the word cannot be found.

'''