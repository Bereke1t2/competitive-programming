class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if not num%2:
                count =0 
                continue
            count +=1
            if count==3:
                return True
        return False