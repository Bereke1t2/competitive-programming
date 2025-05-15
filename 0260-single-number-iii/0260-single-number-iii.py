class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^=num
        
        index  = 0
        group1 = group2 = 0
        for i in range(32):
            if x>>i & 1:
                index = i
                break
        for num in nums:
            if num>>index & 1:
                group1 ^=num
            else:
                group2 ^=num
        return [group1 , group2]
        