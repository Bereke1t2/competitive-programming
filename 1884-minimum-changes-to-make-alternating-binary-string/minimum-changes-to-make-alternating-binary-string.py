class Solution:
    def minOperations(self, s: str) -> int:
        count1 = count2 = 0
        comp1 , comp2 = '0' , '1'
        for l in s:
            count1 += comp1==l
            count2 += comp2==l
            comp1 , comp2 = comp2 , comp1
        return min(len(s) - count1 , len(s) - count2)