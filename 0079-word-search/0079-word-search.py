class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row , col = len(board) , len(board[0])
        def dfs(path,r,c,i):
            if len(path)==len(word):
                return True
            if r<0 or c<0 or c>=col or r>=row or [r,c] in path or board[r][c]!=word[i]:
                return False 
            path.append([r,c])
            res = dfs(path,r+1,c,i+1) or dfs(path,r,c+1,i+1) or dfs(path,r,c-1,i+1) or dfs(path,r-1,c,i+1)  
            path.pop()
            return res
        for i in range(row):
            for j in range(col):
                if dfs([],i,j,0):
                    return True
        return False
       

        