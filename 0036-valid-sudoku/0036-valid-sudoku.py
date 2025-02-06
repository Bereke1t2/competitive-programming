class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                num = board[r][c]
                if num == '.':continue
                if num in row[r] or num in col[c] or num in grid[(r//3,c//3)]:
                    return False
                col[c].add(num)
                row[r].add(num)
                grid[(r//3,c//3)].add(num)
        return True
        

                


