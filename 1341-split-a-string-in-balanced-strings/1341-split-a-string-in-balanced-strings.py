class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = r= 0
        count =  0
        for let in s:
            if let =='L':
                l +=1
            else:
                r +=1
            if l==r:
                count +=1
        return count

        