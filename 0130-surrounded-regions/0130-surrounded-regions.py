class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row  , col = len(board) , len(board[0])
        dir = [[-1,0],[0,-1],[1,0],[0,1]]

        def inbound(r, c):
            return (0 <= r < row and 0 <= c < col)

        def dfs(i , j):
            if not inbound(i, j) or board[i][j] != "O":
                return
            
            board[i][j] = "1"

            for i_ch, j_ch in dir:
                dfs(i + i_ch, j + j_ch)
        
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row-1 or j == 0 or j == col - 1:
                    dfs(i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "1":
                    board[i][j] = "O"
        