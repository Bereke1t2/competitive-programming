class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        while columnNumber:
            print(columnNumber)
            res.append(letters[(columnNumber-1)%26])
            if not columnNumber%26:
                columnNumber -=1
            columnNumber //=26
            
        res.reverse()
        return ''.join(res)