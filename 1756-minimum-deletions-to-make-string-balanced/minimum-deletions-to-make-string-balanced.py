class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        b = 0
        for c in s:
            if c=='a':
                if b:
                    b -=1
                    count +=1
            else:
                b +=1
        return count