class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set1 = {num for num in range(left,right+1)}
        set2 = set()
        for nums in ranges:
            set2.update({num for num in range(nums[0],nums[1]+1)})
        return set1<=set2 

       
        