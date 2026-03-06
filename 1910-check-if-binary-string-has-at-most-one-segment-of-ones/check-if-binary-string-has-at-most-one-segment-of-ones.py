class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        index = [i for i in range(len(s)) if s[i]=='1']
        for i in range(1 , len(index)):
            if index[i]- index[i-1]!=1:
                return False
        return True