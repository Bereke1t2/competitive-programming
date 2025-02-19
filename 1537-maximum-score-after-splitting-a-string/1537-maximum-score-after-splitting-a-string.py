class Solution:
    def maxScore(self, s: str) -> int:
        max_s = 0
        zeros = s.count('0')
        ones = s.count('1')
        count_zero=0
        count_one = 0
        for index  , num in enumerate(s):
            if num=='0':
                count_zero +=1
            else:
                count_one +=1
            if index==len(s)-1:
                continue 
            max_s = max(max_s,count_zero+ones-count_one)
        return max_s

        